# Pydantic is a data validation and settings management library for Python. It allows you to define data models using Python classes, and it provides powerful features for validating and parsing data. Pydantic is often used in web development, data processing, and any situation where you need to ensure that the data you're working with adheres to a specific structure or format.

# Pydantic models are defined as subclasses of BaseModel, and you can specify the types of the fields using standard Python type hints. Pydantic will automatically validate the data when you create an instance of the model, and it will raise errors if the data does not conform to the specified types or constraints.
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'sami'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')


new_student = {'age':'32', 'email':'abc@gmail.com'}

# creates a pydantic model instance from the dictionary, and it will automatically validate the data and convert the age to an integer if possible. If the age cannot be converted to an integer, or if the email is not a valid email address, it will raise a validation error.
student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()
print(student_json)