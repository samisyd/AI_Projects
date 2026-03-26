"""
Example demonstrating how to use mcp_use with Airbnb.

This example shows how to connect an LLM to Airbnb through MCP tools
to perform tasks like searching for accommodations.

Special Thanks to https://github.com/openbnb-org/mcp-server-airbnb for the server.
"""

import asyncio
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

from mcp_use import MCPAgent, MCPClient


async def run_airbnb_example():
    """Run an example using Airbnb MCP server."""
    # Load environment variables
    load_dotenv()


    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY is not set")
    openai = ChatOpenAI(
        model="gpt-4o",
        api_key=openai_api_key,
    )

    # config_file = os.path.join(os.path.dirname(__file__), "browser_mcp.json")

    config_file = "airbnb_mcp.json"

    # Create MCPClient from config file    
    try:
        client = MCPClient.from_config_file(config_file)
    except Exception as e:
        raise RuntimeError(f"Failed to load MCP config: {e}")

    llm = ChatOpenAI(model="gpt-4o")
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True,
        system_prompt="""
    When calling airbnb_search, ALWAYS include ALL of the following fields:

    - location: string (e.g., "Los Angeles, California, USA")
    - checkin: string (YYYY-MM-DD)
    - checkout: string (YYYY-MM-DD)
    - adults: integer
    - children: integer (default 0)
    - infants: integer (default 0)

    NEVER omit fields.
    NEVER send null values.
    ALWAYS provide valid defaults (0 if not specified).

        Example:
        {
        "location": "Los Angeles, California, USA",
        "checkin": "2026-03-28",
        "checkout": "2026-03-30",
        "adults": 2,
        "children": 0,
        "infants": 0
        }
        """
    )
    print("\n===== Interactive MCP Chat =====")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'clear' to clear conversation history")
    print("==================================\n")

    try:
        # Run a query to search for accommodations
        result = await agent.run(
            # "Find me a nice place to stay in Los Angeles for 2 adults for this weekend from March 28th to March 30th 2026",
            "Find me a nice place to stay in Los Angeles, California, USA for 2 adults from March 28 to March 30, 2026",
            # "Show me the top 3 options for this weekend. ",
            max_steps=15,
        )
        print(f"\nResult: {result}")
    except Exception as e:
                print("\n--- Agent Error ---")
                print(type(e).__name__)
                print(str(e))
                print("-------------------")
    finally:
        # Ensure we clean up resources properly
        if client.sessions:
            await client.close_all_sessions()


if __name__ == "__main__":
    asyncio.run(run_airbnb_example())