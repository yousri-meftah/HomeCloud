"""Seed script: creates admin user, seeds IP pool."""
import asyncio
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.engine import async_session_factory
from src.db.base import Base
from src.db.engine import engine
from src.models.user import User
from src.models.ip_pool import IPPool
from src.services.security import hash_password


async def seed():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session_factory() as session:
        result = await session.execute(
            User.__table__.select().where(User.email == "admin@homecloud.local")
        )
        if not result.scalar_one_or_none():
            admin = User(
                id=uuid.uuid4(),
                email="admin@homecloud.local",
                password_hash=hash_password("admin"),
                is_verified=True,
            )
            session.add(admin)

        for i in range(2, 255):
            ip = f"10.10.0.{i}"
            result = await session.execute(
                IPPool.__table__.select().where(IPPool.ip == ip)
            )
            if not result.scalar_one_or_none():
                session.add(IPPool(ip=ip, is_allocated=False))

        await session.commit()
        print("Seed complete: admin user + IP pool created.")


if __name__ == "__main__":
    asyncio.run(seed())
