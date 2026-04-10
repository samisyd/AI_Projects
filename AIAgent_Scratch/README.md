# AI Agent Scratch

## Overview

Learn how to build an AI Agent from scratch using Python — no frameworks, no magic, just clean code. This project demonstrates how to create a tool-calling agent (`JarvisAgent`) that can autonomously decide when to invoke external tools (like a weather API) and incorporate the results into its responses.

## How It Works

1. **User sends a query** — e.g., *"What is the temperature in Tokyo today?"*
2. **The agent forwards it to an LLM** (via Groq) with a list of available tools.
3. **The LLM decides** whether to call a tool or respond directly.
4. **If a tool is called**, the agent executes it locally, sends the result back to the LLM, and lets it generate the final answer.
5. **The loop continues** until the LLM produces a final text response (no more tool calls).


## Requirements

- Python 3.11+ (or the version specified in .python-version)
- Dependencies in requirements.txt or pyproject.toml
- - A [Groq API key](https://console.groq.com/)

## Setup

Create and activate a virtual environment, then install dependencies.

## Run

Use the project runner or run the script directly.

Example:

```
uv run .\main.py
```

## Project Structure

- main.py: Entry point
- requirements.txt / pyproject.toml: Dependencies

## Example Output

```
Response from Alex: The current temperature in Tokyo today is 73°F.
```

## Key Concepts

| Concept | Description |
|---|---|
| **Agentic Loop** | The agent keeps calling the LLM in a loop until it gets a final text response (no pending tool calls). |
| **Tool / Function Calling** | Tools are defined as JSON schemas and passed to the LLM. The model decides when and how to invoke them. |
| **Dynamic Dispatch** | Tool functions are resolved at runtime using `globals()`, making the system easily extensible. |

## Tech Stack

- **Python** — Core language
- **Groq SDK** — LLM inference
- **python-dotenv** — Environment variable management


## Notes

Update this README as features are added.
