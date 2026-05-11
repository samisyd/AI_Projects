from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

template = PromptTemplate( 
    template="Write a 5 line poem on {topic}",
    input_variables=["topic"]
)

prompt = template.invoke({"topic":"nature"})
result = model.invoke(prompt)
print(result.content)


