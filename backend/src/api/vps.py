"""VPS endpoints — delegates to vps_controller."""
from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def list_vps():
    pass


@router.post("")
async def create_vps():
    pass


@router.get("/{vps_id}")
async def get_vps(vps_id: str):
    pass


@router.post("/{vps_id}/start")
async def start_vps(vps_id: str):
    pass


@router.post("/{vps_id}/stop")
async def stop_vps(vps_id: str):
    pass


@router.post("/{vps_id}/restart")
async def restart_vps(vps_id: str):
    pass


@router.delete("/{vps_id}")
async def delete_vps(vps_id: str):
    pass
