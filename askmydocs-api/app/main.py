from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes_docs import router as docs_router

app = FastAPI(
    title="askmydocs-api",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(docs_router, prefix="/api/docs", tags=["docs"])

@app.get("/api/ping", tags=["health"])
async def ping():
    return { "status": "ok" }
