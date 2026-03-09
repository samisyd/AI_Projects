from huggingface_hub import InferenceClient
import os

client = InferenceClient(
    provider="together",
    api_key=os.getenv("HF_TOKEN"),
)

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of Belgium?"
        }
    ],
)

print(completion.choices[0].message.content)