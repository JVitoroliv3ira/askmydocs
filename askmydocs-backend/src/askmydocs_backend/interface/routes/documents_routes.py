from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from askmydocs_backend.pipeline.ask_documents import ask_documents_pipeline

router = APIRouter(prefix="/documents")

class AskRequest(BaseModel):
    question: str
    document_name: str
    collection: str = "public"
    top_k: int = 5

class AskResponse(BaseModel):
    answer: str

@router.post("/ask", response_model=AskResponse)
def ask(payload: AskRequest) -> AskResponse:
    result = ask_documents_pipeline(
        payload.question,
        payload.document_name,
        payload.collection,
        payload.top_k
    )
    
    if result.is_ok():
        return AskResponse(answer=result.ok)
    
    raise HTTPException(
        status_code=400,
        detail=str(result.error)
    )
