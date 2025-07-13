from fastapi import FastAPI
from askmydocs_backend.interface.routes.documents_routes import router as documents_router

app = FastAPI(help="ask-my-docs API")

app.include_router(documents_router, prefix="/api")
