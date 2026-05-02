"""Cloudflare Tunnel service."""


class TunnelService:
    def create_tunnel(self, name: str) -> dict:
        raise NotImplementedError

    def create_dns_record(self, hostname: str, tunnel_id: str) -> dict:
        raise NotImplementedError

    def delete_tunnel(self, tunnel_id: str) -> None:
        raise NotImplementedError

    def list_tunnels(self) -> list[dict]:
        raise NotImplementedError
