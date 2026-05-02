"""AI endpoints — delegates to ai_controller."""
from fastapi import APIRouter

router = APIRouter()


@router.post("/chat")
async def chat():
    pass
