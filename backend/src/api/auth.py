"""Auth endpoints — delegates to auth_controller."""
from fastapi import APIRouter

router = APIRouter()


@router.post("/register")
async def register():
    pass


@router.post("/login")
async def login():
    pass


@router.post("/refresh")
async def refresh_token():
    pass


@router.get("/verify/{token}")
async def verify_email(token: str):
    pass
