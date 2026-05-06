import json
from langfuse.langchain import CallbackHandler
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
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

# --- Step 1: Fetch Prompt created in UI ---
fetched_prompt = lf.get_prompt("Customer_support", version="1")
# --- Step 2: Print raw metadata (pretty JSON) ---
print("\n📌 Prompt Metadata")
print(json.dumps(fetched_prompt.__dict__, indent=2, default=str))

'''
output:
📌 Prompt Metadata
{
  "name": "Customer_support",
  "version": 1,
  "config": {},
  "labels": [
    "latest"
  ],
  "tags": [],
  "commit_message": null,
  "is_fallback": false,
  "prompt": [
    {
      "type": "message",
      "role": "system",
      "content": "You are a helpful support agent"
    },
    {
      "type": "message",
      "role": "user",
      "content": "{{user_query}}"
    }
  ]
}
'''

# --- Step 3: Compile prompt with variables ---
compiled_prompt = fetched_prompt.compile(user_query="How do I reset my password for gmail?")
# --- Step 4: Pretty-print compiled messages ---
print("\n📝 Compiled Prompt Messages")
if isinstance(compiled_prompt, list):  # Chat-style messages
    for i, msg in enumerate(compiled_prompt, 1):
        role = msg.get("role", "unknown").capitalize()
        content = msg.get("content", "")
        print(f"\nMessage {i} ({role}):\n{content}")
else:  # Single string
    print("\nCompiled Prompt:\n", compiled_prompt)

'''
Output:
📝 Compiled Prompt Messages

Message 1 (System):
You are a helpful support agent

Message 2 (User):
How do I reset my password?
'''

# --- Step 5: Run with Ollama ---
response = chain.invoke(compiled_prompt)
print("🤖 UI-created Prompt Response:", response)




