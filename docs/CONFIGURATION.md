# Configuration Guide

## Overview

SigmaXim Prospecter V3 uses environment variables for configuration, managed through Pydantic Settings for type safety and validation.

## Configuration File

Create a `.env` file in the project root. Copy from `.env.example`:

```bash
cp .env.example .env
```

## Configuration Options

### Application Settings

```bash
# Application name (default: sigmaxim-prospecter-v3)
APP_NAME=sigmaxim-prospecter-v3

# Application version (default: 0.1.0)
APP_VERSION=0.1.0

# Environment: development, staging, production, test (default: development)
ENVIRONMENT=development

# Enable debug mode (default: false)
DEBUG=true

# Logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL (default: INFO)
LOG_LEVEL=INFO
```

### AI Service Configuration

```bash
# Google AI Studio API Key
GOOGLE_AI_API_KEY=your_google_ai_api_key_here

# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# Anthropic API Key
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

### Database Configuration

```bash
# SQLite (default)
DATABASE_URL=sqlite:///./data/prospecter.db

# PostgreSQL
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# MySQL
DATABASE_URL=mysql://user:password@localhost:3306/dbname
```

### API Configuration

```bash
# Maximum API requests per minute (1-1000, default: 60)
MAX_REQUESTS_PER_MINUTE=60

# API request timeout in seconds (1-300, default: 30)
API_TIMEOUT_SECONDS=30
```

### Caching

```bash
# Enable caching (default: true)
CACHE_ENABLED=true

# Cache time-to-live in seconds (default: 3600)
CACHE_TTL_SECONDS=3600
```

## Environment-Specific Configuration

### Development

```bash
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=DEBUG
```

### Staging

```bash
ENVIRONMENT=staging
DEBUG=false
LOG_LEVEL=INFO
```

### Production

```bash
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=WARNING
```

## Using Configuration in Code

### Loading Settings

```python
from src.config.settings import get_settings

# Get cached settings instance
settings = get_settings()

# Access configuration values
print(settings.app_name)
print(settings.log_level)
```

### Custom Settings

```python
from src.config.settings import Settings

# Create settings with overrides
settings = Settings(
    environment="test",
    debug=True,
    log_level="DEBUG"
)
```

## Validation

Configuration values are automatically validated:

```python
# Valid log levels
LOG_LEVEL=DEBUG    # ✓
LOG_LEVEL=INFO     # ✓
LOG_LEVEL=WARNING  # ✓
LOG_LEVEL=ERROR    # ✓
LOG_LEVEL=CRITICAL # ✓
LOG_LEVEL=INVALID  # ✗ Raises ValidationError

# Valid environments
ENVIRONMENT=development  # ✓
ENVIRONMENT=staging      # ✓
ENVIRONMENT=production   # ✓
ENVIRONMENT=test         # ✓
ENVIRONMENT=other        # ✗ Raises ValidationError

# Valid rate limits
MAX_REQUESTS_PER_MINUTE=60    # ✓
MAX_REQUESTS_PER_MINUTE=0     # ✗ Must be > 0
MAX_REQUESTS_PER_MINUTE=2000  # ✗ Must be <= 1000
```

## Security Best Practices

### Never Commit Secrets

- Add `.env` to `.gitignore` ✓
- Never commit API keys or passwords
- Use `.env.example` for documentation

### Use Strong Keys

```bash
# Generate a secure secret key
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### Environment-Specific Secrets

Use different API keys for each environment:

```bash
# Development
GOOGLE_AI_API_KEY=dev_key_here

# Production
GOOGLE_AI_API_KEY=prod_key_here
```

## Configuration Precedence

Configuration is loaded in this order (later overrides earlier):

1. Default values in Settings class
2. Values from `.env` file
3. System environment variables
4. Values passed to Settings constructor

## Examples

### Minimal Configuration

```bash
# .env (development)
DEBUG=true
LOG_LEVEL=DEBUG
```

### Production Configuration

```bash
# .env (production)
APP_NAME=sigmaxim-prospecter-v3
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=WARNING

# AI Services
GOOGLE_AI_API_KEY=prod_google_key
OPENAI_API_KEY=prod_openai_key

# Database
DATABASE_URL=postgresql://user:pass@db.example.com:5432/prospecter

# Performance
MAX_REQUESTS_PER_MINUTE=100
API_TIMEOUT_SECONDS=60
CACHE_ENABLED=true
CACHE_TTL_SECONDS=7200
```

## Troubleshooting

### Configuration Not Loading

1. Check `.env` file exists in project root
2. Verify file encoding is UTF-8
3. Ensure no syntax errors in `.env`
4. Check for quotes around values (usually not needed)

### Validation Errors

```python
from pydantic import ValidationError
from src.config.settings import Settings

try:
    settings = Settings()
except ValidationError as e:
    print(e.json())  # See detailed validation errors
```

### Missing Required Values

Some configurations are optional, but you'll see warnings in logs:

```
WARNING - API key not configured for google. Set the appropriate environment variable.
```

## Testing Configuration

### Use Test Settings

```python
import pytest
from src.config.settings import Settings

@pytest.fixture
def test_settings():
    return Settings(
        environment="test",
        debug=True,
        log_level="DEBUG",
        database_url="sqlite:///:memory:"
    )

def test_with_settings(test_settings):
    # Use test_settings in your test
    pass
```

### Override Environment

```python
from unittest.mock import patch
import os

with patch.dict(os.environ, {"LOG_LEVEL": "DEBUG"}):
    settings = Settings()
    assert settings.log_level == "DEBUG"
```

## Reference

### Complete Settings Class

See `src/config/settings.py` for the complete Settings class definition with all available configuration options.

### Type Information

All settings have type hints:
- `str`: String values
- `int`: Integer values
- `bool`: Boolean values (true/false)
- `Optional[str]`: Optional string values

### Default Values

See `.env.example` for all default values and documentation.
