"""VPS instance model."""
import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID, INET
from src.db.base import Base


class VPSInstance(Base):
    __tablename__ = "vps_instances"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    proxmox_vmid = Column(Integer, nullable=True)
    plan = Column(String(20), nullable=False)
    status = Column(String(20), nullable=False, default="provisioning")
    hostname = Column(String(255), nullable=True)
    tunnel_id = Column(String(255), nullable=True)
    ssh_username = Column(String(50), nullable=True)
    ssh_password_enc = Column(String(500), nullable=True)
    internal_ip = Column(INET, nullable=True)
    created_at = Column(String(50))
    started_at = Column(String(50), nullable=True)
