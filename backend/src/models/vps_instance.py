"""VPS instance model."""

import uuid

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.dialects.postgresql import INET, UUID
from sqlalchemy.orm import relationship

from src.db.base import Base
from src.enums.vps_status import VPSStatus


class VPSInstance(Base):
    __tablename__ = "vps_instances"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    proxmox_vmid = Column(Integer, nullable=True)
    plan = Column(String(20), nullable=False)
    status = Column(String(20), nullable=False, default=VPSStatus.PROVISIONING.value)
    hostname = Column(String(255), nullable=True)
    tunnel_id = Column(String(255), nullable=True)
    ssh_username = Column(String(50), nullable=True)
    ssh_password_enc = Column(String(500), nullable=True)
    internal_ip = Column(INET, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    started_at = Column(DateTime(timezone=True), nullable=True)

    owner = relationship("User", back_populates="vps_instances")
    ip_allocation = relationship("IPPool", back_populates="vps")
