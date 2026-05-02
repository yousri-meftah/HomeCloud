"""IP pool model."""
from sqlalchemy import Column, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, INET
from src.db.base import Base


class IPPool(Base):
    __tablename__ = "ip_pool"

    ip = Column(INET, primary_key=True)
    is_allocated = Column(Boolean, default=False)
    vps_id = Column(UUID(as_uuid=True), ForeignKey("vps_instances.id"), nullable=True)
