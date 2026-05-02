"""Multi-env-file loader. Reads all envs/.env.* files before settings init."""
import os
from pathlib import Path


def load_env_files(envs_dir: Path | None = None) -> None:
    """Load every .env.* file from the envs/ directory into the environment."""
    from dotenv import load_dotenv

    if envs_dir is None:
        envs_dir = Path(__file__).resolve().parents[2] / "envs"

    if not envs_dir.is_dir():
        return

    for env_file in sorted(envs_dir.glob(".env.*")):
        load_dotenv(env_file, override=False)


# Auto-load on import
load_env_files()
