# AI Platform Compatibility Guide

## Overview

This document explains how SigmaXim Prospecter V3 is designed to be compatible with multiple AI platforms and how to effectively use it with different AI assistants.

## Supported AI Platforms

### Google AI Studio
- **Status**: Primary development platform
- **Integration**: Direct API support via `AIService`
- **Configuration**: Set `GOOGLE_AI_API_KEY` in `.env`

### OpenAI (ChatGPT, GPT-4)
- **Status**: Fully supported
- **Integration**: Via `AIService` with provider="openai"
- **Configuration**: Set `OPENAI_API_KEY` in `.env`

### Anthropic (Claude)
- **Status**: Fully supported
- **Integration**: Via `AIService` with provider="anthropic"
- **Configuration**: Set `ANTHROPIC_API_KEY` in `.env`

### Cursor AI
- **Status**: Optimized with `.cursorrules`
- **Features**: Code completion, refactoring, documentation
- **Usage**: Open project in Cursor, rules auto-apply

### GitHub Copilot
- **Status**: Compatible
- **Features**: Code suggestions, completion
- **Usage**: Works with standard Python patterns and docstrings

## Design Features for AI Compatibility

### 1. Clear Code Structure

```python
# Good: Clear, self-documenting structure
class Lead:
    """Represents a prospect/lead in the system."""
    
    def __init__(self, name: str, email: str) -> None:
        """Initialize a Lead instance."""
        self.name = name
        self.email = email
```

### 2. Comprehensive Documentation

Every module, class, and function has:
- Purpose description
- Parameter documentation
- Return value documentation
- Usage examples
- Type hints

### 3. Type Safety

```python
from typing import List, Optional

def process_leads(leads: List[Lead]) -> dict:
    """Process leads and return results."""
    pass
```

### 4. Consistent Patterns

All modules follow the same structure:
- Module docstring
- Imports
- Constants
- Classes/Functions
- Main execution

### 5. Meaningful Names

```python
# Good: Self-explanatory
def score_lead(lead: Lead) -> float:
    """Calculate quality score for a lead."""
    pass

# Avoid: Cryptic names
def sl(l: Lead) -> float:
    pass
```

## Using with Different AI Assistants

### Cursor AI

1. **Setup**:
   - Open project in Cursor
   - `.cursorrules` automatically loaded
   - AI understands project context

2. **Features**:
   ```
   # Ask Cursor to:
   - "Add a new feature to score leads by industry"
   - "Refactor this function to be more efficient"
   - "Generate tests for this class"
   - "Explain what this code does"
   ```

3. **Best Practices**:
   - Use natural language commands
   - Reference specific files or functions
   - Ask for explanations when needed

### ChatGPT / Claude

1. **Provide Context**:
   ```
   I'm working on SigmaXim Prospecter V3, a Python prospecting tool.
   The codebase uses Pydantic for settings, type hints throughout,
   and follows PEP 8 standards.
   ```

2. **Ask Specific Questions**:
   ```
   - "How do I add a new AI provider to AIService?"
   - "Write a test for the score_lead function"
   - "Refactor this code to use async/await"
   ```

3. **Share Code Snippets**:
   - Include relevant imports
   - Provide surrounding context
   - Mention file paths

### GitHub Copilot

1. **Write Descriptive Comments**:
   ```python
   # Calculate lead score based on industry match, company size, and engagement
   def score_lead(lead: Lead) -> float:
       # Copilot will suggest implementation
   ```

2. **Use Type Hints**:
   ```python
   def process_leads(leads: List[Lead]) -> Dict[str, Any]:
       # Copilot understands expected types
   ```

3. **Follow Patterns**:
   - Copilot learns from existing code
   - Consistent patterns = better suggestions

## Project Files for AI Context

### `.cursorrules`
Guidelines for Cursor AI including:
- Code style preferences
- Architecture principles
- Testing requirements
- Security practices

### `.aidigestignore`
Excludes irrelevant files from AI context:
- Build artifacts
- Dependencies
- Temporary files
- Large data files

### `.editorconfig`
Ensures consistent formatting:
- Indentation
- Line endings
- Character encoding

## AI-Friendly Documentation

### Module-Level Docstrings

```python
"""
Module description and purpose.

Key features:
- Feature 1
- Feature 2

Example:
    >>> from module import Class
    >>> obj = Class()
"""
```

### Function Docstrings

```python
def function(param: str) -> bool:
    """One-line summary.
    
    Detailed description if needed.
    
    Args:
        param: Description of parameter
        
    Returns:
        Description of return value
        
    Example:
        >>> function("test")
        True
    """
```

### Inline Comments

```python
# Explain WHY, not WHAT
# Good: Calculate weighted score to prioritize recent engagement
score = base_score * recency_weight

# Avoid: Calculate score
score = base_score * recency_weight
```

## Code Organization for AI Understanding

### Logical File Structure

```
src/
├── core/          # Business logic (AI looks here first)
├── services/      # External integrations
├── utils/         # Helper functions
└── config/        # Configuration
```

### Imports Organization

```python
# 1. Standard library
import os
from typing import List

# 2. Third-party
from pydantic import BaseModel

# 3. Local
from src.core.prospecter import Lead
```

### Class Organization

```python
class MyClass:
    """Class docstring."""
    
    # 1. Class variables
    default_value = 10
    
    # 2. __init__
    def __init__(self) -> None:
        pass
    
    # 3. Public methods
    def public_method(self) -> None:
        pass
    
    # 4. Private methods
    def _private_method(self) -> None:
        pass
```

## Testing with AI Assistance

### Generate Tests

```python
# With Cursor or ChatGPT:
"Generate pytest tests for the Prospecter class"
"Add edge case tests for score_lead function"
"Create integration test for AI service"
```

### Review Tests

```python
# Ask AI to:
"Review these tests for completeness"
"Suggest additional test cases"
"Check for missing edge cases"
```

## Extending the Codebase

### Adding New Features

1. **Describe to AI**:
   ```
   "I want to add email validation to the Lead class.
   It should validate email format on initialization."
   ```

2. **Review Suggestions**:
   - Check type hints
   - Verify documentation
   - Ensure tests included

3. **Refine**:
   ```
   "Make the error message more descriptive"
   "Add a custom exception class"
   ```

### Refactoring

1. **Identify Code**:
   ```
   "This function is too long. Help me refactor it."
   ```

2. **Specify Constraints**:
   ```
   "Keep the same interface"
   "Maintain backward compatibility"
   "Add type hints to new functions"
   ```

## Best Practices for AI Collaboration

### 1. Be Specific

❌ "Fix this code"
✅ "Refactor this function to use list comprehension instead of a for loop"

### 2. Provide Context

❌ "Add validation"
✅ "Add email validation to the Lead class using the validate_email utility function"

### 3. Ask for Explanations

```
"Explain how the score_lead function works"
"Why is this implemented this way?"
"What are the trade-offs of this approach?"
```

### 4. Request Documentation

```
"Add docstrings to all functions in this file"
"Generate usage examples for this class"
"Create a README section explaining this feature"
```

### 5. Iterate

```
1. "Create a basic implementation"
2. "Add error handling"
3. "Add type hints"
4. "Generate tests"
5. "Optimize for performance"
```

## Troubleshooting AI Interactions

### AI Suggests Incompatible Code

- Provide more context about dependencies
- Reference existing patterns in codebase
- Specify version constraints

### AI Doesn't Understand Structure

- Share `.cursorrules` content
- Explain architecture principles
- Point to similar existing code

### AI Generates Inconsistent Style

- Reference `.editorconfig`
- Point to PEP 8 compliance
- Show existing code examples

## Resources

- [Code Structure](ARCHITECTURE.md)
- [Usage Examples](USAGE.md)
- [Contributing Guidelines](../CONTRIBUTING.md)
- [Configuration Guide](CONFIGURATION.md)
