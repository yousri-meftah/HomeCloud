"""Admin endpoints — delegates to admin_controller."""
from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
async def list_users():
    pass


@router.get("/vps")
async def list_vps():
    pass


@router.get("/search")
async def search(q: str):
    pass
