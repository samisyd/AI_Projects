# Llamindex-Projects

Small, hands-on experiments using **LlamaIndex** for retrieval-augmented generation (RAG).

## What’s in here

- **`Basic Rag/`**: a minimal RAG notebook that loads PDFs from a local `data/` folder, builds a `VectorStoreIndex`, and queries it using OpenAI.
- **`Llama2_with_llamaindex.ipynb`**: a Colab-style notebook showing a RAG setup using Llama 2 + Hugging Face tooling.
- **`main.py`**: a tiny sanity-check entrypoint.

## Requirements

- **Python**: `3.13` (see `.python-version`)
- **An OpenAI API key** for the OpenAI-backed RAG notebook (`OPENAI_API_KEY`)

## Setup

This repo includes `pyproject.toml` and `uv.lock`, so `uv` is the easiest path.

```bash
uv sync
```

If you prefer plain `pip`, you can install the minimal notebook deps instead:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r "Basic Rag/requirements.txt"
```

## Environment variables

Create a `.env` file (recommended in `Basic Rag/`) with:

```env
OPENAI_API_KEY=your_key_here
```

Notes:
- Don’t commit secrets. If you already have a real `.env`, keep it local only.

## Run

### Run the simple entrypoint

```bash
python main.py
```

### Run the Basic RAG notebook

1. Put documents in `Basic Rag/data/` (the notebook expects a `data` folder next to the notebook).
2. Start Jupyter from the repo root or inside `Basic Rag/`:

```bash
jupyter lab
```

3. Open `Basic Rag/test.ipynb` and run the cells.

The notebook can also persist an index to `Basic Rag/storage/` so you don’t have to rebuild embeddings every run.

### Run the Llama2 + Hugging Face notebook

Open `Llama2_with_llamaindex.ipynb` in Jupyter or upload it to Google Colab. It installs its own dependencies via `pip` cells and is designed for a GPU runtime.

## Repo layout (high level)

```text
.
├─ Basic Rag/
│  ├─ test.ipynb
│  ├─ requirements.txt
│  └─ storage/               # persisted index artifacts (generated)
├─ Llama2_with_llamaindex.ipynb
├─ main.py
├─ pyproject.toml
├─ uv.lock
└─ .python-version
```