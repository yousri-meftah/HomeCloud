"""VPS request/response schemas."""
from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class VPSCreate(BaseModel):
    plan: str
    ssh_public_key: Optional[str] = None


class VPSResponse(BaseModel):
    id: UUID
    plan: str
    status: str
    hostname: Optional[str]
    created_at: datetime
    started_at: Optional[datetime]

    model_config = {"from_attributes": True}


class VPSDetail(VPSResponse):
    ssh_username: Optional[str]
    internal_ip: Optional[str]
    tunnel_id: Optional[str]
