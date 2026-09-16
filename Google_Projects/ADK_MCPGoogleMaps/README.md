# ADK MCP Google Maps

This project demonstrates two Google Maps agent patterns built with the Google Agent Development Kit (ADK):

- `MapsAgent/agent.py` uses direct Google Maps REST APIs (`Directions` and `Places Nearby Search`) via Python `requests`.
- `MCPMapsAgent/agent.py` uses the Google-hosted Maps MCP server at `https://mapstools.googleapis.com/mcp`.

Both are designed to help a conversational agent answer location questions such as:

- get directions between two places
- search for nearby places along a route
- return a Google Maps link when useful

## Project structure

```text
ADK_MCPGoogleMaps/
├── .adk/
├── .env
├── .gitignore
├── .python-version
├── pyproject.toml
├── requirements.txt
├── README.md
├── MapsAgent/
│   └── agent.py
├── MCPMapsAgent/
│   ├── agent.py
│   └── readme.txt
└── uv.lock
```

## Prerequisites

- Python 3.13+
- A Google Cloud project
- A Google Maps API key
- Access to the Maps APIs used by your selected agent
- Optional but recommended: Google Cloud SDK (`gcloud`) for ADC login and local auth

## Environment setup

1. Create a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

or with the project metadata:

```powershell
pip install -e .
```

3. Configure your environment variables in a `.env` file:

```env
GOOGLE_API_KEY="your_google_api_key"
MAPS_API_KEY="your_maps_api_key"
GOOGLE_CLOUD_PROJECT="your_google_cloud_project_id"
```

> Keep your keys out of version control. The repository already contains a local `.env`, but you should replace the values with your own and ensure they are not committed to Git.

## Google Cloud requirements for the MCP version

The MCP-based agent depends on the remote server at `https://mapstools.googleapis.com/mcp` and may require the following in Google Cloud Console:

- enable the Maps Grounding Lite API (or the Maps MCP service associated with `mapstools.googleapis.com`)
- ensure your active project matches `GOOGLE_CLOUD_PROJECT`
- verify your API key is allowed to use the required Maps APIs
- authenticate local ADC if the MCP server uses Application Default Credentials

If you hit a 403 error, the troubleshooting steps in `MCPMapsAgent/readme.txt` are the most relevant reference.

## Running the project

### Option 1: Run the ADK web UI

From the project root:

```powershell
adk web
```

Then open the local ADK web interface in your browser and select the agent you want to test.

### Option 2: Run a specific agent directly

You can also run the Python agent modules directly when appropriate for your local development workflow.

## Agent details

### `MapsAgent`

This version directly calls:

- Google Directions API
- Google Places Nearby Search API

It exposes two tools:

- `get_directions(origin, destination, mode="driving")`
- `search_places_on_route(origin, destination, place_type)`

It is a good fit when you want explicit control over API calls and a simple custom tool layer.

### `MCPMapsAgent`

This version uses `MCPToolset` and the remote Maps MCP server instead of custom HTTP calls. It is useful when you want to rely on Google-provided MCP tooling and a more declarative integration model.

## Example usage

Example prompts to try in the ADK web interface:

- "Give me driving directions from Seattle to Portland."
- "Find a gas station near the route from Atlanta to Miami."
- "Find coffee shops near the midpoint of my trip from New York to Boston."

## Notes

- The app is intentionally lightweight and focused on Maps-related tools.
- The MCP version is more dependent on Google Cloud project configuration and service enablement.
- The direct REST version is simpler to debug if you want to understand the exact API payloads and responses.

## Troubleshooting

Common issues:

- `MAPS_API_KEY` not set
- wrong or missing `GOOGLE_CLOUD_PROJECT`
- Maps Grounding Lite API not enabled
- API key restrictions blocking the required Google Maps service
- local ADC not logged in for MCP access

If you see permission or 403 errors, re-authenticate ADC:

```powershell
& "C:\Users\samin\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd" auth application-default login
```

Then restart the ADK server and test again.

## License

This project is intended for local development and experimentation. Add your preferred license if you plan to share or publish it.
