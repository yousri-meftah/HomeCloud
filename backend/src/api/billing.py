"""Billing endpoints — delegates to billing_controller."""
from fastapi import APIRouter

router = APIRouter()


@router.get("/plans")
async def get_plans():
    pass


@router.post("/checkout")
async def create_checkout():
    pass


@router.post("/webhook")
async def handle_webhook():
    pass


@router.get("/subscription")
async def get_subscription():
    pass
