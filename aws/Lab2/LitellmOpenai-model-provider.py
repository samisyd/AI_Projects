# Import necessary libraries
import os                                     # For accessing environment variables
from strands import Agent                    # Import the Agent class from strands library
# from strands.models.anthropic import AnthropicModel  # Import Anthropic's language model
from strands.models.litellm import LiteLLMModel  # Import LiteLLM model for lightweight LLM capabilities
from strands_tools import generate_image,current_time # Import image generator and current time tools
from dotenv import load_dotenv               # For loading environment variables from .env file

# litellm is a lightweight LLM provider that can be used to access various LLMs, 
# including OpenAI's GPT models. It provides a simple interface for integrating 
# LLMs into your applications.

load_dotenv()

# # Configure the Anthropic language model (Claude)
# model = AnthropicModel(
#     # Set up authentication using API key from environment variables
#     client_args={
#         "api_key": os.getenv("api_key"),  # Get API key from environment variables
#     },
#     # **model_config
#     max_tokens=1028,                    # Set maximum response length to 1028 tokens
#     model_id="anthropic.claude-sonnet-4-6",  # Specify which Claude model version to use
#     params={
#         "temperature": 0.3,              # Set temperature to 0.3 (lower values make output more deterministic)
#     }
# )

# Initialize the LiteLLM model provider configured for OpenAI
model = LiteLLMModel(
    model_id="openai/gpt-4o",  # LiteLLM format: 'openai/<model_name>'    
    params={
        "temperature": 0.2,
        "api_key": os.environ.get("OPENAI_API_KEY"), # Optional if set in environment
        "max_tokens": 200
    }    
)

# Initialize the Strands Agent using the LiteLLM model wrapper
agent = Agent(
    model=model,
    system_prompt="You are a helpful, concise AI assistant. Answer in 2-3 lines",
    tools=[current_time]
)

# Run the agent
response = agent("What is time in New York City?")
print(response)

# Create a general-purpose AI agent with AWS capabilities
# agent = Agent(
#     model=model,                      # Use the Anthropic model configured above
#     tools=[generate_image,current_time]  # Give the agent access to the image generator and current time tools
# )

# Define a query 
# query = "Generate an image of a husky surfing on a surfboard in the Philippines. Also share the current time after you generate the image"

# Send the query to the agent and store the response
# response = agent(query)