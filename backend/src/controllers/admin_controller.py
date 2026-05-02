"""Admin business logic."""


async def list_users() -> list[dict]:
    raise NotImplementedError


async def list_vps() -> list[dict]:
    raise NotImplementedError


async def search(query: str) -> dict:
    raise NotImplementedError
