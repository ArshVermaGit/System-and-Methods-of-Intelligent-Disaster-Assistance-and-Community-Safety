"""Application settings and configuration management."""

from functools import lru_cache
from pathlib import Path
from typing import List, Optional, Union

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

REPO_ROOT = Path(__file__).resolve().parents[3]
ENV_FILE_PATH = REPO_ROOT / ".env"


class Settings(BaseSettings):
    """NIRVYX application configuration settings."""

    model_config = SettingsConfigDict(
        env_file=str(ENV_FILE_PATH),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # General & Application Info
    APPLICATION_NAME: str = "NIRVYX"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"
    SECRET_KEY: str = "change-this-to-a-secure-random-secret-key-in-production"

    # Server Bindings
    BACKEND_HOST: str = "0.0.0.0"
    BACKEND_PORT: int = 8000

    # CORS
    ALLOWED_ORIGINS: Union[List[str], str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]

    # Database
    DATABASE_URL: Optional[str] = None
    TEST_DATABASE_URL: Optional[str] = None

    # Storage and Processing Limits
    STORAGE_DIR: str = "results"
    MAX_UPLOAD_MB: int = 200
    MAX_PIXELS: int = 25_000_000

    # Machine Learning Models
    MODEL_MODE: str = "real"  # "real" or "mock"
    MODEL_DEVICE: str = "cpu"
    FLOOD_PREDICTOR: str = "flood.predict"
    LANDSLIDE_PREDICTOR: str = "landslide.predict"
    FLOOD_CHECKPOINT_PATH: Optional[str] = None
    LANDSLIDE_CHECKPOINT_PATH: Optional[str] = None

    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def parse_allowed_origins(cls, value: Union[str, List[str]]) -> List[str]:
        """Parse comma-separated string into list of origins."""
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",") if origin.strip()]
        return value

    @property
    def storage_path(self) -> Path:
        """Resolve storage path relative to repo root."""
        path = Path(self.STORAGE_DIR)
        if not path.is_absolute():
            return REPO_ROOT / path
        return path


@lru_cache()
def get_settings() -> Settings:
    """Return cached singleton settings instance."""
    return Settings()
