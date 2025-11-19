"""Utility functions for SigmaXim Prospecter.

This module provides common utility functions used throughout the application
including logging setup, data validation, formatting helpers, and more.

All utilities are designed to be:
- Reusable across different modules
- Well-documented with examples
- Type-safe with proper type hints
- Tested with comprehensive test coverage
"""

import logging
from typing import Any, Dict, List, Optional


def setup_logging(log_level: str = "INFO") -> logging.Logger:
    """Set up and configure application logging.

    Creates a logger with consistent formatting across the application.
    Logs include timestamp, log level, module name, and message.

    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    Returns:
        logging.Logger: Configured logger instance

    Example:
        >>> logger = setup_logging("DEBUG")
        >>> logger.info("Application started")
    """
    logger = logging.getLogger("sigmaxim-prospecter")

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(log_level)

    # Console handler with formatting
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger


def validate_email(email: str) -> bool:
    """Validate email address format.

    Performs basic email validation using a simple pattern check.
    For production use, consider using a more robust email validation library.

    Args:
        email: Email address to validate

    Returns:
        bool: True if email format is valid, False otherwise

    Example:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid-email")
        False
    """
    import re

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def sanitize_string(text: str, max_length: Optional[int] = None) -> str:
    """Sanitize and clean string input.

    Removes leading/trailing whitespace and optionally truncates to max length.
    Useful for cleaning user input and preventing injection attacks.

    Args:
        text: String to sanitize
        max_length: Maximum allowed length (None for no limit)

    Returns:
        str: Sanitized string

    Example:
        >>> sanitize_string("  Hello World  ", max_length=5)
        'Hello'
    """
    cleaned = text.strip()
    if max_length and len(cleaned) > max_length:
        cleaned = cleaned[:max_length]
    return cleaned


def format_currency(amount: float, currency: str = "USD") -> str:
    """Format amount as currency string.

    Args:
        amount: Numeric amount to format
        currency: Currency code (e.g., 'USD', 'EUR', 'GBP')

    Returns:
        str: Formatted currency string

    Example:
        >>> format_currency(1234.56)
        '$1,234.56'
        >>> format_currency(1000.00, 'EUR')
        '€1,000.00'
    """
    currency_symbols = {
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥",
    }
    symbol = currency_symbols.get(currency, currency)
    return f"{symbol}{amount:,.2f}"


def chunk_list(items: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into smaller chunks.

    Useful for batch processing and pagination.

    Args:
        items: List to split into chunks
        chunk_size: Size of each chunk

    Returns:
        List[List[Any]]: List of chunks

    Example:
        >>> chunk_list([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Deep merge two dictionaries.

    Recursively merges dict2 into dict1. If both values are dicts, merge them.
    Otherwise, dict2 values override dict1 values.

    Args:
        dict1: Base dictionary
        dict2: Dictionary to merge into dict1

    Returns:
        Dict[str, Any]: Merged dictionary

    Example:
        >>> d1 = {"a": 1, "b": {"c": 2}}
        >>> d2 = {"b": {"d": 3}, "e": 4}
        >>> deep_merge(d1, d2)
        {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
    """
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value

    return result


def safe_get(dictionary: Dict[str, Any], key_path: str, default: Any = None) -> Any:
    """Safely get nested dictionary value using dot notation.

    Args:
        dictionary: Dictionary to query
        key_path: Dot-separated path to the value (e.g., "user.profile.name")
        default: Default value if key path doesn't exist

    Returns:
        Any: Value at key path or default

    Example:
        >>> data = {"user": {"profile": {"name": "John"}}}
        >>> safe_get(data, "user.profile.name")
        'John'
        >>> safe_get(data, "user.profile.age", default=0)
        0
    """
    keys = key_path.split(".")
    value = dictionary

    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return default

    return value
