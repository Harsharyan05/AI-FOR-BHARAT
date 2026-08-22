"""
Application Configuration

Loads environment variables and application settings.

Author: Harsh Aryan
Project: Cognisys
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from .env
    """

    PROJECT_NAME: str
    API_VERSION: str

    DEBUG: bool

    DATABASE_URL: str

    GOOGLE_API_KEY: str = ""

    OPENAI_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()
# ----------------------------
# RAG Settings
# ----------------------------

TOP_K: int = 10

MAX_HISTORY: int = 10

MAX_CHUNK_LENGTH: int = 1500