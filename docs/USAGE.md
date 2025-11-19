# Usage Guide

## Getting Started

This guide covers common usage patterns for SigmaXim Prospecter V3.

## Basic Usage

### Running the Prospecter

```python
from src.core.prospecter import Prospecter

# Initialize the prospecter
prospecter = Prospecter()

# Run with default settings
results = prospecter.run()

# Access results
print(f"Processed: {results['total_processed']} leads")
print(f"Qualified: {results['total_qualified']} leads")
print(f"Average score: {results['average_score']:.2f}")
```

### Creating Leads

```python
from src.core.prospecter import Lead

# Create a simple lead
lead = Lead(
    name="Acme Corporation",
    email="contact@acme.com"
)

# Create a detailed lead
lead = Lead(
    name="Tech Innovations Inc",
    email="sales@techinnovations.com",
    industry="Technology",
    company_size=250,
    metadata={
        "website": "https://techinnovations.com",
        "last_contact": "2024-01-15",
        "source": "LinkedIn"
    }
)
```

### Scoring Leads

```python
from src.core.prospecter import Lead, Prospecter

prospecter = Prospecter()

# Score a single lead
lead = Lead(name="Example Co", email="info@example.com")
score = prospecter.score_lead(lead)
print(f"Lead score: {score:.2f}")

# Access the score from the lead object
print(f"Lead {lead.name} has score: {lead.score:.2f}")
```

### Processing Multiple Leads

```python
from src.core.prospecter import Lead, Prospecter

prospecter = Prospecter()

# Create a list of leads
leads = [
    Lead(name="Company A", email="a@example.com", industry="Tech", company_size=100),
    Lead(name="Company B", email="b@example.com", industry="Finance", company_size=500),
    Lead(name="Company C", email="c@example.com", industry="Retail", company_size=50),
]

# Process and sort by score
processed_leads = prospecter.process_leads(leads)

# Display results
for lead in processed_leads:
    print(f"{lead.name}: {lead.score:.2f}")
```

### Filtering by Score

```python
from src.core.prospecter import Prospecter

prospecter = Prospecter()

# Only get high-quality leads (score >= 0.7)
results = prospecter.run(min_score=0.7)

# Access qualified leads
for lead_dict in results['qualified_leads']:
    print(f"{lead_dict['name']}: {lead_dict['score']:.2f}")
```

## Advanced Usage

### Custom Configuration

```python
from src.config.settings import Settings
from src.core.prospecter import Prospecter

# Create custom settings
settings = Settings(
    log_level="DEBUG",
    environment="production"
)

# Use custom settings
prospecter = Prospecter(settings=settings)
results = prospecter.run()
```

### Working with AI Services

```python
from src.services.ai_service import AIService

# Initialize AI service with specific provider
ai_service = AIService(provider="google")

# Generate text
response = ai_service.generate_text(
    prompt="Analyze this prospect...",
    temperature=0.7,
    max_tokens=500
)

# Analyze lead data
lead_data = {
    "name": "Tech Corp",
    "industry": "Software",
    "company_size": 150
}
analysis = ai_service.analyze_lead(lead_data)
print(analysis['insights'])
```

### Using Different AI Providers

```python
from src.services.ai_service import AIService

# Google AI
google_ai = AIService(provider="google")

# OpenAI
openai_ai = AIService(provider="openai")

# Anthropic
anthropic_ai = AIService(provider="anthropic")
```

### Batch Processing

```python
from src.core.prospecter import Lead, Prospecter
from src.utils.helpers import chunk_list

prospecter = Prospecter()

# Large list of leads
all_leads = [...]  # Your lead list

# Process in batches
batch_size = 100
for batch in chunk_list(all_leads, batch_size):
    results = prospecter.run(leads=batch, min_score=0.6)
    # Process results...
```

## Utility Functions

### Email Validation

```python
from src.utils.helpers import validate_email

email = "user@example.com"
if validate_email(email):
    print("Valid email")
else:
    print("Invalid email")
```

### String Sanitization

```python
from src.utils.helpers import sanitize_string

# Remove whitespace
clean = sanitize_string("  hello world  ")
# Result: "hello world"

# Truncate to length
short = sanitize_string("very long string", max_length=10)
# Result: "very long "
```

### Currency Formatting

```python
from src.utils.helpers import format_currency

# USD (default)
print(format_currency(1234.56))
# Output: "$1,234.56"

# EUR
print(format_currency(1000.00, "EUR"))
# Output: "€1,000.00"
```

### Safe Dictionary Access

```python
from src.utils.helpers import safe_get

data = {
    "user": {
        "profile": {
            "name": "John Doe"
        }
    }
}

# Safe nested access
name = safe_get(data, "user.profile.name")
# Result: "John Doe"

# With default for missing keys
age = safe_get(data, "user.profile.age", default=0)
# Result: 0
```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# Application Settings
APP_NAME=my-prospecter
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=INFO

# AI Service Keys
GOOGLE_AI_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here

# Database
DATABASE_URL=postgresql://user:pass@localhost/db

# Feature Flags
ENABLE_AI_SCORING=true
ENABLE_ANALYTICS=true
```

### Loading Configuration

```python
from src.config.settings import get_settings

# Get singleton settings instance
settings = get_settings()

# Access settings
print(settings.app_name)
print(settings.log_level)
print(settings.google_ai_api_key)
```

## Error Handling

### Handling Validation Errors

```python
from pydantic import ValidationError
from src.config.settings import Settings

try:
    settings = Settings(log_level="INVALID")
except ValidationError as e:
    print(f"Configuration error: {e}")
```

### Logging Errors

```python
from src.utils.helpers import setup_logging

logger = setup_logging("INFO")

try:
    # Your code here
    pass
except Exception as e:
    logger.error(f"Error occurred: {e}", exc_info=True)
```

## Best Practices

### 1. Always Validate Input

```python
from src.utils.helpers import validate_email, sanitize_string

email = sanitize_string(user_input_email)
if not validate_email(email):
    raise ValueError("Invalid email address")
```

### 2. Use Type Hints

```python
from typing import List
from src.core.prospecter import Lead

def process_my_leads(leads: List[Lead]) -> dict:
    """Process leads and return summary."""
    # Implementation
    pass
```

### 3. Handle Errors Gracefully

```python
from src.core.prospecter import Prospecter

prospecter = Prospecter()

try:
    results = prospecter.run()
except Exception as e:
    logger.error(f"Failed to run prospecter: {e}")
    # Handle error appropriately
```

### 4. Use Logging Instead of Print

```python
from src.utils.helpers import setup_logging

logger = setup_logging("INFO")

# Good
logger.info("Processing started")

# Avoid
print("Processing started")
```

## Examples

### Complete Workflow Example

```python
from src.core.prospecter import Lead, Prospecter
from src.config.settings import get_settings
from src.utils.helpers import setup_logging

# Setup
settings = get_settings()
logger = setup_logging(settings.log_level)
prospecter = Prospecter()

# Create leads
leads = [
    Lead(
        name="Tech Startup Inc",
        email="contact@techstartup.com",
        industry="Technology",
        company_size=50
    ),
    Lead(
        name="Enterprise Corp",
        email="sales@enterprise.com",
        industry="Finance",
        company_size=1000
    ),
]

# Process leads
logger.info(f"Processing {len(leads)} leads")
results = prospecter.run(leads=leads, min_score=0.6)

# Display results
logger.info(f"Qualified {results['total_qualified']} leads")
for lead in results['qualified_leads']:
    logger.info(f"  {lead['name']}: {lead['score']:.2f}")
```

## Troubleshooting

### Issue: AI service not working
**Solution**: Ensure API keys are set in `.env` file

### Issue: Import errors
**Solution**: Ensure you're in the project root and virtual environment is activated

### Issue: Configuration not loading
**Solution**: Check that `.env` file exists and has correct format

## Next Steps

- Read [ARCHITECTURE.md](ARCHITECTURE.md) for system design
- See [CONTRIBUTING.md](../CONTRIBUTING.md) for development guidelines
- Check [README.md](../README.md) for setup instructions
