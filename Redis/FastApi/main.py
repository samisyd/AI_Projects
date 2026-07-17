# Entry Point & Lifespan Context

# This file handles application startup, attaches the API router, and runs the lifespan lifecycle.

from contextlib import asynccontextmanager
from fastapi import FastAPI

from config import rag_service
from routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize models and Redis
    print("Initializing RAG Service and Redis Cache...")
    rag_service.initialize()
    yield
    # Shutdown logic (if needed)
    print("Shutting down API...")


app = FastAPI(
    title="RAG & Semantic Cache API",
    lifespan=lifespan,
)

# Attach the router
app.include_router(router)