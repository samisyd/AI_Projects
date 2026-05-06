from langfuse.langchain import CallbackHandler
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langfuse import Langfuse
import os
from dotenv import load_dotenv

load_dotenv()

langfuse_handler = CallbackHandler()

llm = ChatOpenAI(model_name="gpt-4.1-mini", callbacks=[langfuse_handler])
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
parser = StrOutputParser()
chain = prompt | llm | parser

# Set trace attributes dynamically via metadata
response = chain.invoke(
    {"topic": "cats"},
    config={
        "metadata": {
            "langfuse_user_id": "sami-user",
            "langfuse_session_id": "sami-session",
            "langfuse_tags": ["langchain-1", "langfuseDemo-tag-2"]
        }
    }
)

print(response)

'''
output:
Why did the cat sit on the computer? Because it wanted to keep an eye on the mouse
'''

