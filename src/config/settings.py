"""Configuration management for SigmaXim Prospecter.

This module handles all application configuration including environment variables,
settings validation, and configuration management across different environments.

The configuration is loaded from environment variables and .env files, with
proper validation using Pydantic for type safety.

Example:
    >>> from src.config.settings import get_settings
    >>> settings = get_settings()
    >>> print(settings.app_name)
    'sigmaxim-prospecter-v3'
"""

from functools import lru_cache
from typing import Optional

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with validation.

    All settings are loaded from environment variables or .env file.
    Type hints ensure proper validation of configuration values.

    Attributes:
        app_name: Name of the application
        app_version: Version of the application
        environment: Deployment environment (development, staging, production)
        debug: Enable debug mode
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        google_ai_api_key: API key for Google AI services
        openai_api_key: API key for OpenAI services
        anthropic_api_key: API key for Anthropic services
        database_url: Database connection URL
        max_requests_per_minute: Rate limit for API requests
        api_timeout_seconds: Timeout for external API calls
        cache_enabled: Enable caching
        cache_ttl_seconds: Cache time-to-live in seconds
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application Settings
    app_name: str = Field(default="sigmaxim-prospecter-v3")
    app_version: str = Field(default="0.1.0")
    environment: str = Field(default="development")
    debug: bool = Field(default=False)
    log_level: str = Field(default="INFO")

    # AI Service API Keys
    google_ai_api_key: Optional[str] = Field(default=None)
    openai_api_key: Optional[str] = Field(default=None)
    anthropic_api_key: Optional[str] = Field(default=None)

    # Database Configuration
    database_url: str = Field(default="sqlite:///./data/prospecter.db")

    # API Configuration
    max_requests_per_minute: int = Field(default=60, gt=0, le=1000)
    api_timeout_seconds: int = Field(default=30, gt=0, le=300)

    # Caching
    cache_enabled: bool = Field(default=True)
    cache_ttl_seconds: int = Field(default=3600, gt=0)

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        """Validate log level is one of the standard logging levels.

        Args:
            v: Log level string to validate

        Returns:
            Validated and uppercased log level

        Raises:
            ValueError: If log level is not valid
        """
        valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
        v_upper = v.upper()
        if v_upper not in valid_levels:
            raise ValueError(f"log_level must be one of {valid_levels}")
        return v_upper

    @field_validator("environment")
    @classmethod
    def validate_environment(cls, v: str) -> str:
        """Validate environment is one of the allowed values.

        Args:
            v: Environment string to validate

        Returns:
            Validated and lowercased environment

        Raises:
            ValueError: If environment is not valid
        """
        valid_envs = {"development", "staging", "production", "test"}
        v_lower = v.lower()
        if v_lower not in valid_envs:
            raise ValueError(f"environment must be one of {valid_envs}")
        return v_lower


@lru_cache()
def get_settings() -> Settings:
    """Get cached application settings.

    This function uses lru_cache to ensure settings are loaded only once
    and reused across the application.

    Returns:
        Settings: Application settings instance

    Example:
        >>> settings = get_settings()
        >>> print(settings.app_name)
        'sigmaxim-prospecter-v3'
    """
    return Settings()
