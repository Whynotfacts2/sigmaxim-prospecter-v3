"""
SigmaXim Prospecter V3

An AI-powered smart prospecting tool designed for multi-platform compatibility.
This package provides intelligent lead scoring, prospecting automation, and
integration with various AI platforms.

Key Features:
    - AI-powered lead scoring and analysis
    - Multi-platform AI compatibility (Google AI Studio, OpenAI, Anthropic, etc.)
    - Modular and extensible architecture
    - Comprehensive error handling and logging
    - Type-safe implementations

Example:
    >>> from src.core.prospecter import Prospecter
    >>> prospecter = Prospecter()
    >>> results = prospecter.run()

Author: SigmaXim Team
License: MIT
"""

__version__ = "0.1.0"
__author__ = "SigmaXim Team"
__license__ = "MIT"

# Package-level imports for convenience
from src.core.prospecter import Prospecter
from src.config.settings import Settings

__all__ = [
    "Prospecter",
    "Settings",
]
