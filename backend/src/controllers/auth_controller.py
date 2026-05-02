"""Auth business logic."""


async def register(email: str, password: str) -> dict:
    raise NotImplementedError


async def login(email: str, password: str) -> dict:
    raise NotImplementedError


async def refresh_token(refresh_token: str) -> dict:
    raise NotImplementedError


async def verify_email(token: str) -> dict:
    raise NotImplementedError
