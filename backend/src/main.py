"""HomeCloud Backend - FastAPI Application Entry Point."""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Load all env files before anything else
import src.config.loader  # noqa: F401
from src.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="HomeCloud API",
        description="Personal cloud VPS provisioning platform",
        version="0.1.0",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    from src.api.admin import router as admin_router
    from src.api.ai import router as ai_router
    from src.api.auth import router as auth_router
    from src.api.billing import router as billing_router
    from src.api.vps import router as vps_router

    app.include_router(auth_router, prefix="/auth", tags=["auth"])
    app.include_router(vps_router, prefix="/vps", tags=["vps"])
    app.include_router(billing_router, prefix="/billing", tags=["billing"])
    app.include_router(ai_router, prefix="/ai", tags=["ai"])
    app.include_router(admin_router, prefix="/admin", tags=["admin"])

    @app.get("/health")
    async def health_check():
        return {"status": "ok", "version": "0.1.0"}

    return app


app = create_app()
