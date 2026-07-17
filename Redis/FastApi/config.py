
# Core Services (LLM, Redis, & LangChain)

# This file manages the initialization and cleanup of your Redis Vector Store, Semantic Cache, and LangChain models.

import os
import time
from pathlib import Path
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_redis import RedisVectorStore, RedisSemanticCache
from langchain_core.globals import set_llm_cache

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
BASE_DIR = Path(__file__).resolve().parent

class RAGService:
    def __init__(self):
        self.embeddings = None
        self.llm = None
        self.semantic_cache = None
        self.vector_store = None

    def initialize(self):
        """Initializes embeddings, LLM, cache, and vector store."""
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        self.llm = OpenAI()

        # Configure Semantic Cache
        self.semantic_cache = RedisSemanticCache(
            embeddings=self.embeddings,
            redis_url=REDIS_URL,
            distance_threshold=0.1,
        )
        set_llm_cache(self.semantic_cache)

        # Ingest Document into Vector Store
        pdf_path = BASE_DIR / "data" / "cold_and_flu_r.pdf"
        if pdf_path.is_file():
            loader = PyPDFLoader(str(pdf_path))
            documents = loader.load()
            self.vector_store = RedisVectorStore.from_documents(
                documents=documents,
                embedding=self.embeddings,
                redis_url=REDIS_URL,
                index_name="document_embeddings",
            )
            print("Vector store initialized successfully.")
        else:
            print(f"Warning: PDF file not found at {pdf_path}. Ingestion skipped.")

    def query(self, question: str):
        """Retrieves context and invokes LLM (utilizing RedisSemanticCache)."""
        if not self.vector_store:
            raise RuntimeError("Vector store is not initialized.")

        start_time = time.time()

        retriever = self.vector_store.as_retriever()
        docs = retriever.invoke(question)

        context = "\n".join([doc.page_content for doc in docs])
        formatted_prompt = f"Context: {context}\n\nQuestion: {question}"

        response_text = self.llm.invoke(formatted_prompt)
        execution_time = time.time() - start_time

        return {
            "question": question,
            "answer": response_text.strip(),
            "execution_time_seconds": round(execution_time, 3),
        }

    def clear_cache(self):
        """Clears the LLM semantic cache."""
        if self.semantic_cache:
            self.semantic_cache.clear()
            return True
        return False

# Single global instance
rag_service = RAGService()