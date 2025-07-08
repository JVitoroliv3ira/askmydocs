from fastapi import APIRouter

router = APIRouter()

@router.post("/upload")
async def upload():
    return { "status": "processing" }