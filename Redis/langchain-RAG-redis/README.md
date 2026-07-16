# LangChain + Redis Example

This project demonstrates a simple Retrieval-Augmented Generation (RAG) workflow using LangChain, OpenAI, and Redis.

It loads a PDF document from the data folder, stores its embeddings in a Redis vector index, and uses Redis semantic caching to speed up repeated prompts.

## What this project does

- Reads a PDF file from the data directory
- Creates embeddings with OpenAI
- Stores those embeddings in Redis using Redis Vector Store
- Uses Redis semantic caching for similar prompts
- Runs basic example queries against the indexed document

## Requirements

- Python 3.13+
- Redis running locally or a reachable Redis instance
- An OpenAI API key

## Environment variables

Create a .env file in the project root with:

```env
OPENAI_API_KEY=your_openai_api_key
REDIS_URL=redis://localhost:6379
```

## Installation

Using uv:

```bash
uv sync
```

Or with pip:

```bash
pip install -r requirements.txt
```

## Run the example

```bash
uv run python test.py
```

The example will:

1. Connect to Redis
2. Load the PDF from data/cold_and_flu_r.pdf
3. Create a vector index in Redis
4. Run a first query and a semantically similar follow-up query

## Project structure

- main.py - simple entry point
- test.py - main demo script for Redis vector search and semantic caching
- data/ - sample PDF documents
- pyproject.toml - project dependencies and metadata

## Notes

- If Redis is not running, start it locally before running the example.
- If the PDF file is missing, place your own PDF in the data folder and update the path in test.py if needed.
