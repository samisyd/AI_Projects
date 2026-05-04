from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

import os

load_dotenv()

class Review(BaseModel):

    author : str  = Field(description="The name of the reviewer")
    sentiment : Literal["positive", "negative", "neutral"] = Field(description="The sentiment of the review")

model = ChatOpenAI(model="gpt-4o-mini")

structured_model = model.with_structured_output(Review)
result = structured_model.invoke("The product is amazing and I love it! Review by Samina")    
print(result)

