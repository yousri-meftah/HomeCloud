"""Billing request/response schemas."""
from pydantic import BaseModel


class PlanResponse(BaseModel):
    name: str
    cpu: int
    ram_mb: int
    disk_gb: int
    price_monthly: float


class CheckoutResponse(BaseModel):
    session_id: str
    checkout_url: str
