"""Proxmox VE service."""


class ProxmoxService:
    def __init__(self):
        self._client = None

    def clone_template(self, name: str, plan: str) -> str:
        raise NotImplementedError

    def poll_task(self, upid: str, timeout: int = 120) -> dict:
        raise NotImplementedError

    def start_vm(self, vmid: int) -> None:
        raise NotImplementedError

    def stop_vm(self, vmid: int) -> None:
        raise NotImplementedError

    def restart_vm(self, vmid: int) -> None:
        raise NotImplementedError

    def delete_vm(self, vmid: int) -> None:
        raise NotImplementedError

    def get_vm_status(self, vmid: int) -> dict:
        raise NotImplementedError

    def set_cloudinit_config(self, vmid: int, config: dict) -> None:
        raise NotImplementedError

    def list_vms(self) -> list[dict]:
        raise NotImplementedError
