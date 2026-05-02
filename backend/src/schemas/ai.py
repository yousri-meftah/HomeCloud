"""AI chat request/response schemas."""
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[ChatMessage]
    vps_id: Optional[UUID] = None


class ChatResponse(BaseModel):
    content: str
