# RAG + Redis Semantic Cache with FastAPI

This project is a simple Retrieval-Augmented Generation (RAG) application built with FastAPI, LangChain, OpenAI, Redis, and a PDF-based knowledge source. It ingests a local document into a Redis vector store and uses Redis semantic caching to speed up repeated or similar questions.

## Features

- Query a PDF-backed knowledge base through a FastAPI endpoint
- Use Redis vector search for document retrieval
- Cache semantically similar LLM responses with Redis
- Serve a lightweight browser-based frontend from the root route
- Clear the semantic cache through an API endpoint

## Project Structure

- `main.py` – FastAPI app entry point and startup lifecycle
- `routes.py` – API routes for the frontend and query handling
- `config.py` – RAG service logic, document ingestion, Redis setup, and LLM calls
- `index.html` – Simple web UI for testing the app
- `data/` – Folder containing the PDF document used as the knowledge base for the RAG pipeline
- `data/cold_and_flu_r.pdf` – Sample document used for retrieval

## Prerequisites

- Python 3.13+
- Redis running locally on `localhost:6379` (or set `REDIS_URL` in your environment)
- An OpenAI API key

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   REDIS_URL=redis://localhost:6379
   ```

4. Make sure Redis is running.

## Run the Application

Start the FastAPI app with:

```bash
uvicorn main:app --reload
```

Then open:

- `http://127.0.0.1:8000/` for the frontend

## API Endpoints

- `GET /` – Serves the web UI
- `POST /api/query` – Sends a question and returns an answer
  - Example body:
    ```json
    {
      "question": "What is influenza?"
    }
    ```
- `DELETE /api/cache/clear` – Clears the semantic cache

## Notes

- The application will attempt to ingest the PDF from `data/cold_and_flu_r.pdf` on startup.
- If the PDF file is missing, the vector store initialization will be skipped with a warning.
- The semantic cache is useful for repeated or rephrased questions because similar prompts can be answered faster.
