"""VPS request/response schemas."""
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class VPSCreate(BaseModel):
    plan: str
    ssh_public_key: str | None = None


class VPSResponse(BaseModel):
    id: UUID
    plan: str
    status: str
    hostname: str | None
    created_at: datetime
    started_at: datetime | None

    model_config = {"from_attributes": True}


class VPSDetail(VPSResponse):
    ssh_username: str | None
    internal_ip: str | None
    tunnel_id: str | None
