from langfuse.langchain import CallbackHandler
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langfuse import Langfuse
import os
from dotenv import load_dotenv

load_dotenv()
langfuse_handler = CallbackHandler()
parser = StrOutputParser()
llm = ChatOpenAI(model_name="gpt-4.1-mini", callbacks=[langfuse_handler])

chain = llm | parser

# Init Langfuse
lf = Langfuse(
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    host=os.getenv("LANGFUSE_HOST")
)

programmatic_prompt = lf.create_prompt(
    name="Customer_support",   # same slug
    type="chat",               # must match existing type
    prompt=[
        {"role": "system", "content": "You are a poetic support agent. Answer user query in poetic way"},
        {"role": "user", "content": "{{user_query}}"}
    ],
    labels=["latest", "production"],
    config={}
)

print("✅ New Customer_support prompt version:", programmatic_prompt.version)


# Fetch version 2 of the prompt
prompt = lf.get_prompt("Customer_support", version=2)

# Variables for the user query
variables = {"user_query": "How do I reset my password?"}

# Compile prompt with variables
final_prompt = prompt.compile(**variables)  # unpack dict into kwargs

# Print the compiled prompt
print("📝 Final Prompt:")
for msg in final_prompt:
    print(msg)

chain = llm | parser

# Print response directly
print("🤖 Model response:", chain.invoke(final_prompt))

'''
output:
 New Customer_support prompt version: 2
📝 Final Prompt:
{'role': 'system', 'content': 'You are a poetic support agent. Answer user query in poetic way'}
{'role': 'user', 'content': 'How do I reset my password?'}
🤖 Model response: To reset the key that guards your gate,  
Follow these steps—don’t hesitate:  
Seek the "Forgot Password?" light,  
Click it gently, day or night.  

Enter your email, pure and true,  
A link will come, designed for you.  
With that magic thread you’ll find,  
A path to leave old keys behind.  

Set a new code, strong and bright,  
Guard it well, with all your might.  
And thus your portal will restore,  
Access granted, evermore.
'''


