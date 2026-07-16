# LangChain Apps with Redis

This project is a small repository for building LangChain-based applications with Redis. It includes notebooks that demonstrate common patterns such as caching, chat history, and vector search using Redis.

## What’s included

- A simple Python entry point in [main.py](main.py)
- Three notebook examples that show different Redis use cases in LangChain:
  - [caching.ipynb](caching.ipynb): demonstrates both standard and semantic caching for LLM responses using Redis. It compares the first and second call to the same prompt and shows how Redis can reduce repeated model latency.
  - [chat_history.ipynb](chat_history.ipynb): shows how to store and retrieve conversational history with Redis using `RedisChatMessageHistory`. It demonstrates multi-turn chat behavior and session-based memory.
  - [vector_store.ipynb](vector_store.ipynb): loads sample movie data, creates embeddings, stores documents in Redis as a vector store, and performs similarity search with and without metadata filters.
- Sample movie data in [data/movies.json](data/movies.json)

## Prerequisites

- Python 3.13+
- Docker Desktop (for running Redis locally)
- Optional: [uv](https://docs.astral.sh/uv/) or pip

## Setup

1. Clone the repository and change into the project folder.
2. Install dependencies:

   ```bash
   uv sync
   ```

   Or, if you prefer pip:

   ```bash
   pip install -r requirements.txt
   ```



3. If your notebooks or examples require external APIs, create a `.env` file and add the relevant environment variables.

## Running the project

Run the basic Python entry point:

```bash
python main.py
```

Open the notebooks in Jupyter to explore the Redis-backed examples:

```bash
jupyter notebook
```

## Project structure

```text
.
├── main.py
├── pyproject.toml
├── requirements.txt
├── caching.ipynb
├── chat_history.ipynb
├── vector_store.ipynb
├── data/
│   └── movies.json
└── README.md
```

