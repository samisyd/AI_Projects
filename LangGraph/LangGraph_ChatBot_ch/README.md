# LangGraph PDF Chatbot

A Streamlit chat UI backed by a **LangGraph** agent that can answer from uploaded PDFs (RAG), search the web, run simple arithmetic, and look up stock quotes. Conversations are keyed by **thread ID**; the backend keeps a **FAISS** vector index per thread for PDF retrieval and uses **SQLite** (`chatbot_memory.db`) for LangGraph checkpoint metadata used when listing and loading threads.

## Features

- **PDF RAG**: Upload a PDF in the sidebar; pages are chunked, embedded with OpenAI, and stored in memory for that chat thread. The model can call `rag_tool` to retrieve relevant passages.
- **Tools**: DuckDuckGo web search, a small calculator tool, Alpha Vantage stock quotes, and the PDF retriever.
- **Multi-thread UI**: New chats get a UUID; the sidebar can show saved threads (from the SQLite checkpointer) and reload their message state.

## Requirements

- Python **3.13+** (see `pyproject.toml`; adjust if you use an older interpreter and align dependencies).
- An **OpenAI API key** with access to `gpt-4o-mini` and `text-embedding-3-small`.

## Setup

1. Clone or copy this project and open a terminal in the project root.

2. Create and activate a virtual environment (recommended).

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, if you use **uv** or another tool with `pyproject.toml`:

   ```bash
   uv sync
   ```

4. Create a `.env` file in the project root with at least:

   ```env
   OPENAI_API_KEY=sk-...
   ```

   Optional: set `LANGCHAIN_TRACING_V2`, `LANGCHAIN_API_KEY`, etc., if you use [LangSmith](https://smith.langchain.com/) tracing.

## Run the app

From the project root:

```bash
streamlit run streamlit_frontend_rag.py
```

Then open the URL Streamlit prints (usually `http://localhost:8501`).

**Typical flow**

1. Type a message to start a new thread (or use **New chat** / pick an existing thread in the sidebar).
2. Upload a **PDF** for that thread when you want document-grounded answers.
3. Ask questions; the agent may call search, calculator, stock, or RAG tools as needed.

## Project layout

| File | Role |
|------|------|
| `streamlit_frontend_rag.py` | Streamlit UI: threads, PDF upload, chat streaming. |
| `chatbot_rag_backend.py` | LangGraph graph, tools, FAISS ingestion per thread, SQLite checkpointer. |
| `main.py` | Minimal placeholder entrypoint (`Hello from chatbot-langgraph!`). |
| `requirements.txt` / `pyproject.toml` | Dependencies and project metadata. |
| `chatbot_memory.db` | Created at runtime: SQLite DB for graph checkpoints (thread discovery). |

## Development note

The UI loads prior messages from `chatbot_with_memory` when you pick a thread in the sidebar, but the live chat stream uses the graph compiled **without** the checkpointer. To persist every new turn into `chatbot_memory.db`, point the Streamlit app at `chatbot_with_memory` for `invoke` / `stream` (same `config` with `thread_id`).

## Configuration notes

- **Stock tool**: Price lookups use the [Alpha Vantage](https://www.alphavantage.co/support/#api-key) API. For production or sharing the repo, move the API key out of source code into an environment variable (for example `ALPHA_VANTAGE_API_KEY`) and read it in `get_stock_price` instead of hardcoding it.
- **In-memory RAG**: PDF indexes live in process memory (`_THREAD_RETRIEVERS`). Restarting the app clears them; users need to re-upload PDFs after a restart even if thread history still appears in SQLite.
- **DuckDuckGo**: Search behavior uses `region="us-en"` in the backend; change in `chatbot_rag_backend.py` if you need another locale.

## License

Add a license file if you distribute this project; none is specified in the repository by default.
