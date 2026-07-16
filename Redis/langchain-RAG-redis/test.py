import os
import redis
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

# Test Redis connection
redis_client = redis.from_url(REDIS_URL)
print("Printing the ping result:", redis_client.ping())

# Imports
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAI, OpenAIEmbeddings

# Use langchain_redis for BOTH the cache and vector store
from langchain_redis import RedisVectorStore, RedisSemanticCache
from langchain_core.globals import set_llm_cache

# 1. Initialize Embeddings & LLM
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
llm = OpenAI()

# 2. Configure Global Semantic Cache using langchain_redis
semantic_cache = RedisSemanticCache(
        embeddings=embeddings,
        redis_url=REDIS_URL,
        distance_threshold=0.1,
    )

# 2. Assign it to global LLM cache
set_llm_cache(semantic_cache)

# 3. Load PDF
# loader = PyPDFLoader("./data/cold_and_flu.pdf")
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

# Resolve the directory of test4.py, then build the path to the PDF
SCRIPT_DIR = Path(__file__).resolve().parent
pdf_path = SCRIPT_DIR / "data" / "cold_and_flu_r.pdf"

# Verify the file actually exists before attempting to load
if not pdf_path.is_file():
    raise FileNotFoundError(f"PDF not found at expected path: {pdf_path}")

loader = PyPDFLoader(str(pdf_path))
documents = loader.load()

# 4. Initialize Vector Store using from_documents
vector_store = RedisVectorStore.from_documents(
    documents=documents,
    embedding=embeddings,  # Note: from_documents uses 'embedding' singular
    redis_url=REDIS_URL,
    index_name="document_embeddings",
)

# query = "What is Influenza?"
# scored_results = vector_store.similarity_search_with_score(query, k=1)
# for doc, score in scored_results:
#     print(doc, score)


def execute_with_timing(prompt):
    start_time = time.time()
    result = llm.invoke(prompt)
    end_time = time.time()
    return result, end_time - start_time

# 5. Query
retriever = vector_store.as_retriever()
docs = retriever.invoke("What is Influenza?")

context = "\n".join([doc.page_content for doc in docs])
formatted_prompt = f"Context: {context}\n\nQuestion: What is Influenza?"
# First execution (Cache Miss)
result1, time1 = execute_with_timing(formatted_prompt)
print(f"First call (not cached):")
print(f"{result1}\nTime: {time1:.2f} seconds\n")


# Second execution (Cache Hit)
print("\n--- Running semantically similar query ---")
formatted_prompt2 = f"Context: {context}\n\nQuestion: Tell me about influenza?"
result2, time2 = execute_with_timing(formatted_prompt2)
print(f"Second call (cached):")
print(f"{result2}\nTime: {time2:.2f} seconds\n")


# Delete the underlying index and it's data
vector_store.index.delete(drop=True)

# Clear the semantic cache entries and index
semantic_cache.clear() # Clears cached responses
print("Vector store and semantic cache successfully cleared!")