"""SSH service for VM provisioning."""


class SSHService:
    async def wait_for_ssh_ready(self, ip: str, port: int = 22, timeout: int = 90) -> bool:
        raise NotImplementedError

    async def execute_remote_commands(
        self,
        ip: str,
        commands: list[str],
        username: str = "ubuntu",
        password: str = "",
    ) -> str:
        raise NotImplementedError

    async def install_cloudflared(
        self,
        ip: str,
        username: str = "ubuntu",
        password: str = "",
    ) -> None:
        raise NotImplementedError

    async def start_cloudflared_service(
        self,
        ip: str,
        tunnel_token: str,
        username: str = "ubuntu",
        password: str = "",
    ) -> None:
        raise NotImplementedError
