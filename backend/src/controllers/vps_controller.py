"""VPS business logic."""


async def list_vps(user_id: str) -> list[dict]:
    raise NotImplementedError


async def create_vps(user_id: str, plan: str, ssh_public_key: str | None = None) -> dict:
    raise NotImplementedError


async def get_vps(vps_id: str, user_id: str) -> dict:
    raise NotImplementedError


async def start_vps(vps_id: str, user_id: str) -> dict:
    raise NotImplementedError


async def stop_vps(vps_id: str, user_id: str) -> dict:
    raise NotImplementedError


async def restart_vps(vps_id: str, user_id: str) -> dict:
    raise NotImplementedError


async def delete_vps(vps_id: str, user_id: str) -> dict:
    raise NotImplementedError
