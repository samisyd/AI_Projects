# mcp-use-test

Small playground repo showing how to use **[`mcp_use`](https://pypi.org/project/mcp-use/)** to connect an LLM (LangChain) to MCP servers like:

- **Playwright MCP** (browser automation)
- **Airbnb MCP** (search stays)
- **DuckDuckGo Search MCP** (web search)
- **Weather MCP** (NWS alerts + forecast)

This repo also includes a small **flight booking** MCP server (`flightBooking.py`).

The MCP servers are configured in JSON files like:

- `browser_mcp.json`
- `airbnb_mcp.json`
- `flight_booking.json`

These are loaded via `MCPClient.from_config_file(...)`.
Note: `browser_mcp.json` is the “main” config and includes Playwright + Airbnb + DuckDuckGo + Weather + Flight booking.

## Requirements

- **Python**: \(>= 3.13\) (see `pyproject.toml`)
- **Node.js**: needed because the MCP servers are launched via `npx`

## Setup

Create a virtualenv, then install deps:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

If you use `uv`, you can also do:

```bash
uv sync
```

## Environment variables

Create a `.env` file in the repo root with the keys you need:

```bash
OPENAI_API_KEY="..."
GROQ_API_KEY="..."
```

Notes:
- `app.py` requires **`OPENAI_API_KEY`**
- `airbnb.py` requires **`GROQ_API_KEY`**

## Run

### Interactive MCP chat (browser + other MCP servers)

This starts an interactive loop and uses `browser_mcp.json` (includes Weather and Flight booking too):

```bash
python app.py
```

Type:
- `exit` / `quit` to stop
- `clear` to clear the agent’s conversation history

### Airbnb example

Runs a single Airbnb-focused prompt using `airbnb_mcp.json`:

```bash
python airbnb.py
```

### Flight booking MCP server

This repo includes an MCP server that exposes:

- Resources: `file://airports`, `file://airlines`
- Tools: `search_flights`, `create_booking`
- Prompts: `find_best_flight`, `handle_disruption`

The server configuration is in `flight_booking.json`.

### Weather MCP server

The Weather MCP server is implemented in `weather.py` and makes live requests to the US National Weather Service (NWS) API at `https://api.weather.gov`.

Tools it exposes:

- `get_alerts(state: str)` (e.g. `CA`, `NY`)
- `get_forecast(latitude: float, longitude: float)` (returns the next few forecast periods)

Run via the interactive app by using `browser_mcp.json`, or start the server yourself (depending on your MCP setup).

## Files

- `app.py`: interactive chat using `ChatOpenAI` + `MCPAgent` + `browser_mcp.json`
- `airbnb.py`: example using `ChatGroq` + Airbnb MCP tools
- `flightBooking.py`: example MCP server (airports/airlines + flight search/booking)
- `browser_mcp.json`: MCP server definitions (launched with `npx`)
- `weather.py`: MCP server for NWS alerts and forecast
- `main.py`: placeholder “Hello” script

## Troubleshooting

- **`npx` not found**: install Node.js and ensure it’s on your PATH.
- **MCP config load error**: confirm `browser_mcp.json` is in the repo root and valid JSON.
- **API key errors**: ensure `.env` exists and the required key is set.