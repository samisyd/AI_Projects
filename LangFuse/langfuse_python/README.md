# Langfuse Python Demo

A small demo project showing how to use Langfuse with Python and LangChain/OpenAI.

## Project Overview

This repository contains example scripts for working with Langfuse to:
- create Langfuse prompts programmatically
- read prompts created in the Langfuse UI
- invoke language models with LangChain and OpenAI
- send Langfuse callback telemetry and tracing metadata

## Files

- `.git/` - Git repository metadata.
- `.gitignore` - Files and directories ignored by Git.
- `.python-version` - Python version for the project.
- `.venv/` - Local virtual environment directory.
- `uv.lock` - lock file created by `uv` for reproducible dependencies.
- `requirements.txt` - project dependencies list for pip.
- `pyproject.toml` - project metadata and dependency configuration.
- `README.md` - this file.

### Python scripts

- `main.py`
  - A simple console chat loop using `langfuse.openai.OpenAI`.
  - Sends a system prompt and user input to `gpt-4.1-mini` and prints the model output.

- `langchaindemo.py`
  - Demonstrates a minimal Langfuse + OpenAI chat example.
  - Uses the Langfuse OpenAI wrapper directly for chat completions.

- `langfuse_prompt.py`
  - Fetches an existing prompt from Langfuse using `Langfuse.get_prompt()`.
  - Prints prompt metadata and compiled prompt messages.
  - Invokes the compiled prompt through a LangChain pipeline.

- `langfuse_createPrompt.py`
  - Creates or updates a Langfuse prompt programmatically with `Langfuse.create_prompt()`.
  - Fetches a specific prompt version, compiles it with variables, and invokes it.

## Installation

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Alternatively, if using `uv` and `pyproject.toml`:

```powershell
uv install
```

## Environment Variables

The examples use `python-dotenv` to load environment variables from a `.env` file.

Create a `.env` file in the project root with values like:

```env
LANGFUSE_SECRET_KEY=your_secret_key
LANGFUSE_PUBLIC_KEY=your_public_key
LANGFUSE_HOST=https://api.langfuse.com
OPENAI_API_KEY=your_openai_api_key
```

Adjust keys as required by your Langfuse and OpenAI setup.

## Usage

Run the example scripts individually from the project folder:

```powershell
python main.py
python langchaindemo.py
python langfuse_prompt.py
python langfuse_createPrompt.py
```

### Notes

- `langfuse_prompt.py` expects a prompt named `Customer_support` to already exist in Langfuse.
- `langfuse_createPrompt.py` demonstrates prompt creation and then retrieves version `2` of the same prompt.
- `main.py` and `langchaindemo.py` show direct chat usage with the Langfuse OpenAI integration.

## Dependencies

The project depends on packages listed in `pyproject.toml` and `requirements.txt`, including:

- `langfuse`
- `langchain`
- `langchain-openai`
- `openai`
- `python-dotenv`
- `langgraph`
- `langsmith`

## License

This demo project does not include a license file. Add one if you plan to share or publish the code.
