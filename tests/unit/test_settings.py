"""Unit tests for configuration management.

These tests verify the Settings class and configuration loading.
"""

import os
from unittest.mock import patch

import pytest

from src.config.settings import Settings, get_settings


class TestSettings:
    """Test cases for the Settings class."""

    def test_default_settings(self) -> None:
        """Test that default settings are loaded correctly."""
        settings = Settings()

        assert settings.app_name == "sigmaxim-prospecter-v3"
        assert settings.app_version == "0.1.0"
        assert settings.environment == "development"
        assert settings.log_level == "INFO"

    def test_environment_override(self) -> None:
        """Test that environment variables override defaults."""
        with patch.dict(os.environ, {"APP_NAME": "custom-app", "DEBUG": "true"}):
            settings = Settings()

            assert settings.app_name == "custom-app"
            assert settings.debug is True

    def test_log_level_validation(self) -> None:
        """Test that log level validation works."""
        with patch.dict(os.environ, {"LOG_LEVEL": "debug"}):
            settings = Settings()
            assert settings.log_level == "DEBUG"

        with pytest.raises(ValueError):
            with patch.dict(os.environ, {"LOG_LEVEL": "INVALID"}):
                Settings()

    def test_environment_validation(self) -> None:
        """Test that environment validation works."""
        valid_envs = ["development", "staging", "production", "test"]

        for env in valid_envs:
            with patch.dict(os.environ, {"ENVIRONMENT": env}):
                settings = Settings()
                assert settings.environment == env

        with pytest.raises(ValueError):
            with patch.dict(os.environ, {"ENVIRONMENT": "invalid"}):
                Settings()

    def test_rate_limiting_constraints(self) -> None:
        """Test that rate limiting values are validated."""
        with patch.dict(os.environ, {"MAX_REQUESTS_PER_MINUTE": "100"}):
            settings = Settings()
            assert settings.max_requests_per_minute == 100

    def test_get_settings_caching(self) -> None:
        """Test that get_settings returns cached instance."""
        # Clear cache first
        get_settings.cache_clear()

        settings1 = get_settings()
        settings2 = get_settings()

        assert settings1 is settings2
