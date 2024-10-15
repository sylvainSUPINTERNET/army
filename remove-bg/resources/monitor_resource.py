from fastapi import APIRouter
from fastapi.responses import JSONResponse
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/health")
async def health():
    return JSONResponse(content={"error": "OK"}, status_code=200)