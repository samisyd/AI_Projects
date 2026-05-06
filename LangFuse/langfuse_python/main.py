# https://langfuse.com/self-hosting/deployment/docker-compose

# Langfuse is a tool for tracking and analyzing interactions with language models. It provides insights into how users interact with the models, allowing developers to optimize and improve their applications. The code snippet below demonstrates how to use Langfuse with OpenAI's GPT-4.1-mini model to create a simple chat interface.

from dotenv import load_dotenv
# from openai import OpenAI
from langfuse.openai import OpenAI

load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = """
    You are an AI agent who solves user query within 40 words.
"""

def main():
    while True:
        user_input = input(">")

        if user_input.lower() == 'exit':
            break

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ]
        )
 
        print(response.choices[0].message.content)

main()