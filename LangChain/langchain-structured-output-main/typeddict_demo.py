# TypedDict is a way to define a dictionary with specific keys and value types. It allows you to create a dictionary that has a specific structure, which can help catch errors and improve code readability.
# it doesnt enforce the type of values at runtime, but it can be used with type checkers like mypy to catch type errors during development.
from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'harish', 'age':'35'}

print(new_person)