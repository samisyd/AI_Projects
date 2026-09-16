

# To use Google's remote Maps MCP server ([https://mapstools.googleapis.com/mcp](https://mapstools.googleapis.com/mcp)), you need to enable the Map Tools API (also referenced as mapstools.googleapis.com or Google Maps Platform MCP Service) in your Google Cloud Console.

import os
from dotenv import load_dotenv

from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

load_dotenv()

MAPS_API_KEY = os.getenv("MAPS_API_KEY")

MAPS_MCP_URL = "https://mapstools.googleapis.com/mcp"  # Google-hosted Maps MCP endpoint

maps_toolset = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url=MAPS_MCP_URL,
        headers={
            "X-Goog-Api-Key": MAPS_API_KEY,
        },
    )
)

root_agent = LlmAgent(
    model="gemini-3.1-flash-lite",
    name="MCPMapsAgent",
    # GOOGLE_API_KEY=GOOGLE_API_KEY,
    instruction=(
        "You are a helpful Maps assistant.\n"
        "Use the MCP-provided Maps tools to find places and get directions.\n"
        "When directions are requested, include a Google Maps link in the final answer."
    ),
    tools=[maps_toolset]
)