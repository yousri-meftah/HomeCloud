"""App settings — loaded from all envs/.env.* files by config/loader.py."""
from functools import lru_cache
from typing import Literal

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # App
    APP_ENV: Literal["development", "staging", "production"] = "development"
    DEBUG: bool = False
    CORS_ORIGINS: list[str] = ["http://localhost:3000"]

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://homecloud:homecloud@localhost:5432/homecloud"
    DATABASE_POOL_SIZE: int = 5
    DATABASE_MAX_OVERFLOW: int = 10

    # JWT
    JWT_SECRET: str = "change-me-to-a-secure-random-string"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # Proxmox
    PROXMOX_HOST: str = "192.168.1.10"
    PROXMOX_PORT: int = 8006
    PROXMOX_USER: str = "homecloud@pve"
    PROXMOX_TOKEN_NAME: str = ""
    PROXMOX_TOKEN_VALUE: str = ""
    PROXMOX_VERIFY_SSL: bool = False
    PROXMOX_TEMPLATE_VMID: int = 9000
    PROXMOX_NODE_NAME: str = "pve"

    # Cloudflare
    CLOUDFLARE_API_TOKEN: str = ""
    CLOUDFLARE_ACCOUNT_ID: str = ""
    CLOUDFLARE_ZONE_ID: str = ""
    CLOUDFLARE_DOMAIN: str = "yourdomain.com"

    # Stripe
    STRIPE_SECRET_KEY: str = ""
    STRIPE_WEBHOOK_SECRET: str = ""
    STRIPE_PRICE_ID_SMALL: str = ""
    STRIPE_PRICE_ID_MEDIUM: str = ""
    STRIPE_PRICE_ID_LARGE: str = ""

    # Gemini
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-1.5-flash"

    # Sentry
    SENTRY_DSN: str = ""

    # R2
    R2_ACCESS_KEY_ID: str = ""
    R2_SECRET_ACCESS_KEY: str = ""
    R2_ENDPOINT_URL: str = ""
    R2_BUCKET_NAME: str = "homecloud"

    # Encryption
    ENCRYPTION_KEY: str = ""

    # Elasticsearch
    ELASTICSEARCH_URL: str = "http://localhost:9200"

    # Email
    SMTP_HOST: str = ""
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM: str = "noreply@yourdomain.com"

    # App Settings
    MAX_VPS_PER_USER: int = 3

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
