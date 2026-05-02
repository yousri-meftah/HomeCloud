"""Admin request/response schemas."""
from pydantic import BaseModel


class SearchResponse(BaseModel):
    users: list[dict]
    vps_instances: list[dict]
    total: int
