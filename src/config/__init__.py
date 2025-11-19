"""Configuration package for SigmaXim Prospecter.

This package contains all configuration-related modules including settings
management, environment variable handling, and configuration validation.
"""

from src.config.settings import Settings, get_settings

__all__ = ["Settings", "get_settings"]
