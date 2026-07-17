# FastAPI Router & Request Handlers

# This file defines all API routes and delegates processing to rag_service.


from pathlib import Path
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from config import rag_service

router = APIRouter()
BASE_DIR = Path(__file__).resolve().parent

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    question: str
    answer: str
    execution_time_seconds: float


@router.get("/")
async def serve_frontend():
    """Serves the index.html page."""
    html_file = BASE_DIR / "index.html"
    if not html_file.is_file():
        raise HTTPException(status_code=404, detail="index.html not found.")
    return FileResponse(html_file)


@router.post("/api/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    """Executes a query against the RAG pipeline."""
    try:
        result = rag_service.query(request.question)
        return QueryResponse(**result)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/api/cache/clear")
async def clear_cache():
    """Clears the LLM response semantic cache."""
    success = rag_service.clear_cache()
    if success:
        return {"status": "success", "message": "Semantic cache cleared successfully."}
    raise HTTPException(status_code=500, detail="Semantic cache is not initialized.")