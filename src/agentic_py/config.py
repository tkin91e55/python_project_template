"""Application configuration utilities."""

from __future__ import annotations

from functools import lru_cache
from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    """Settings validated via Pydantic."""

    environment: Literal["development", "testing", "production"] = Field(
        "development",
        description="Active runtime environment profile.",
        alias="AGENTIC_ENVIRONMENT",
    )
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        "INFO",
        description="Default logging verbosity.",
        alias="AGENTIC_LOG_LEVEL",
    )
    registry_capacity: int = Field(
        100,
        ge=1,
        le=1000,
        description="Maximum number of agents permitted in the registry.",
        alias="AGENTIC_REGISTRY_CAPACITY",
    )

    @field_validator("log_level")
    @classmethod
    def normalize_log_level(cls, value: str) -> str:
        """Ensure configured log level is upper-case."""
        return value.upper()

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        populate_by_name=True,
    )


@lru_cache
def get_config() -> AppConfig:
    """Return a cached application configuration instance."""
    return AppConfig()
