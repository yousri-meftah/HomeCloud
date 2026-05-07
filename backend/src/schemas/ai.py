"""AI chat request/response schemas."""
from uuid import UUID

from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[ChatMessage]
    vps_id: UUID | None = None


class ChatResponse(BaseModel):
    content: str
