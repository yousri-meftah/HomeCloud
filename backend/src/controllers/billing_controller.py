"""Billing business logic."""


async def get_plans() -> list[dict]:
    raise NotImplementedError


async def create_checkout(user_id: str, plan: str) -> dict:
    raise NotImplementedError


async def handle_webhook(payload: bytes, signature: str) -> None:
    raise NotImplementedError


async def get_subscription(user_id: str) -> dict:
    raise NotImplementedError
