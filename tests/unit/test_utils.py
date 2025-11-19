"""Unit tests for utility functions.

These tests verify the functionality of helper functions in the utils module.
"""

import pytest

from src.utils.helpers import (
    chunk_list,
    deep_merge,
    format_currency,
    safe_get,
    sanitize_string,
    validate_email,
)


class TestValidateEmail:
    """Test cases for email validation."""

    def test_valid_email(self) -> None:
        """Test that valid email addresses are accepted."""
        assert validate_email("user@example.com") is True
        assert validate_email("test.user@example.co.uk") is True
        assert validate_email("user+tag@example.com") is True

    def test_invalid_email(self) -> None:
        """Test that invalid email addresses are rejected."""
        assert validate_email("invalid") is False
        assert validate_email("@example.com") is False
        assert validate_email("user@") is False
        assert validate_email("user@.com") is False


class TestSanitizeString:
    """Test cases for string sanitization."""

    def test_removes_whitespace(self) -> None:
        """Test that leading/trailing whitespace is removed."""
        assert sanitize_string("  hello  ") == "hello"
        assert sanitize_string("\t\ntest\t\n") == "test"

    def test_respects_max_length(self) -> None:
        """Test that string is truncated to max_length."""
        assert sanitize_string("hello world", max_length=5) == "hello"
        assert sanitize_string("test", max_length=10) == "test"

    def test_no_max_length(self) -> None:
        """Test that string is not truncated without max_length."""
        long_string = "a" * 1000
        assert sanitize_string(long_string) == long_string


class TestFormatCurrency:
    """Test cases for currency formatting."""

    def test_usd_formatting(self) -> None:
        """Test USD currency formatting."""
        assert format_currency(1234.56) == "$1,234.56"
        assert format_currency(0.99, "USD") == "$0.99"

    def test_other_currencies(self) -> None:
        """Test formatting with different currency symbols."""
        assert format_currency(1000.00, "EUR") == "€1,000.00"
        assert format_currency(500.50, "GBP") == "£500.50"


class TestChunkList:
    """Test cases for list chunking."""

    def test_even_chunks(self) -> None:
        """Test chunking with evenly divisible list."""
        items = [1, 2, 3, 4, 5, 6]
        chunks = chunk_list(items, 2)

        assert chunks == [[1, 2], [3, 4], [5, 6]]

    def test_uneven_chunks(self) -> None:
        """Test chunking with remainder."""
        items = [1, 2, 3, 4, 5]
        chunks = chunk_list(items, 2)

        assert chunks == [[1, 2], [3, 4], [5]]

    def test_single_chunk(self) -> None:
        """Test when chunk_size is larger than list."""
        items = [1, 2, 3]
        chunks = chunk_list(items, 10)

        assert chunks == [[1, 2, 3]]


class TestDeepMerge:
    """Test cases for deep dictionary merging."""

    def test_simple_merge(self) -> None:
        """Test merging non-nested dictionaries."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3}
        result = deep_merge(dict1, dict2)

        assert result == {"a": 1, "b": 2, "c": 3}

    def test_nested_merge(self) -> None:
        """Test merging nested dictionaries."""
        dict1 = {"a": {"b": 1, "c": 2}}
        dict2 = {"a": {"c": 3, "d": 4}}
        result = deep_merge(dict1, dict2)

        assert result == {"a": {"b": 1, "c": 3, "d": 4}}

    def test_override_values(self) -> None:
        """Test that dict2 values override dict1."""
        dict1 = {"a": 1}
        dict2 = {"a": 2}
        result = deep_merge(dict1, dict2)

        assert result == {"a": 2}


class TestSafeGet:
    """Test cases for safe nested dictionary access."""

    def test_existing_path(self) -> None:
        """Test retrieving existing nested value."""
        data = {"user": {"profile": {"name": "John"}}}
        assert safe_get(data, "user.profile.name") == "John"

    def test_missing_path(self) -> None:
        """Test retrieving non-existing path returns default."""
        data = {"user": {"profile": {"name": "John"}}}
        assert safe_get(data, "user.profile.age") is None
        assert safe_get(data, "user.profile.age", default=0) == 0

    def test_partial_path(self) -> None:
        """Test retrieving partial path."""
        data = {"user": {"profile": {"name": "John"}}}
        result = safe_get(data, "user.profile")
        assert result == {"name": "John"}
