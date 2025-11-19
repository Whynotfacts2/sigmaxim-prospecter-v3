# Contributing to SigmaXim Prospecter V3

Thank you for your interest in contributing to SigmaXim Prospecter V3! This document provides guidelines and best practices for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Maintain professional communication

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature or fix
4. Make your changes
5. Test thoroughly
6. Submit a pull request

## Development Workflow

### Setting Up Your Development Environment

1. Install Python 3.9 or higher
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

### Making Changes

1. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```

2. **Write Clean Code**
   - Follow PEP 8 style guidelines
   - Use type hints
   - Write comprehensive docstrings
   - Keep functions small and focused
   - Add comments for complex logic

3. **Document Your Changes**
   - Update README.md if needed
   - Add/update docstrings
   - Update relevant documentation in `/docs`
   - Add examples if introducing new features

4. **Write Tests**
   - Add unit tests for new functionality
   - Ensure all tests pass
   - Aim for high test coverage
   - Use descriptive test names

5. **Run Quality Checks**
   ```bash
   # Run tests
   pytest tests/
   
   # Check code style
   ruff check src/ tests/
   
   # Format code
   ruff format src/ tests/
   
   # Type checking
   mypy src/
   ```

### Commit Guidelines

Write clear, descriptive commit messages:

```
<type>: <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Example:**
```
feat: Add lead scoring algorithm

Implement AI-powered lead scoring based on multiple factors
including engagement history, company size, and industry match.

Closes #123
```

### Pull Request Process

1. **Before Submitting**
   - Ensure all tests pass
   - Update documentation
   - Run linting and formatting
   - Rebase on the latest main branch

2. **PR Description**
   - Clearly describe what changes were made
   - Explain why the changes were necessary
   - Reference any related issues
   - Add screenshots for UI changes
   - List any breaking changes

3. **Review Process**
   - Address review feedback promptly
   - Keep discussions professional and constructive
   - Update your PR based on feedback
   - Request re-review when ready

## Code Style Guidelines

### Python Code Style

- Follow PEP 8
- Maximum line length: 100 characters
- Use 4 spaces for indentation
- Use type hints for all functions
- Write docstrings in Google style

**Example:**
```python
from typing import List, Optional

def process_leads(
    leads: List[dict],
    min_score: float = 0.7,
    max_results: Optional[int] = None
) -> List[dict]:
    """Process and filter leads based on scoring criteria.
    
    Args:
        leads: List of lead dictionaries to process
        min_score: Minimum score threshold for filtering
        max_results: Maximum number of results to return (None for all)
    
    Returns:
        List of filtered and scored leads
        
    Raises:
        ValueError: If min_score is not between 0 and 1
    """
    if not 0 <= min_score <= 1:
        raise ValueError("min_score must be between 0 and 1")
    
    # Implementation here
    pass
```

### Documentation Style

- Use clear, concise language
- Include code examples
- Explain the "why" not just the "what"
- Keep documentation up to date

## Testing Guidelines

### Unit Tests

- Test one thing per test
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern
- Mock external dependencies

**Example:**
```python
import pytest
from src.core.prospecter import Prospecter

def test_lead_scoring_returns_valid_score():
    """Test that lead scoring returns a score between 0 and 1."""
    # Arrange
    prospecter = Prospecter()
    lead = {"name": "Test Company", "size": 100}
    
    # Act
    score = prospecter.score_lead(lead)
    
    # Assert
    assert 0 <= score <= 1
```

### Integration Tests

- Test complete workflows
- Use realistic test data
- Clean up resources after tests

## AI Platform Compatibility

When contributing, ensure your code is compatible with multiple AI platforms:

- **Clear Structure**: Use obvious naming and organization
- **Documentation**: Comment complex logic
- **Modularity**: Keep components independent
- **Type Hints**: Help AI understand data types
- **Examples**: Provide usage examples in docstrings

## Security Considerations

- Never commit secrets or API keys
- Use environment variables for sensitive data
- Validate and sanitize all inputs
- Follow security best practices
- Report security vulnerabilities privately

## Questions?

If you have questions about contributing:
- Open an issue with the "question" label
- Review existing issues and documentation
- Contact the maintainers

Thank you for contributing to SigmaXim Prospecter V3!
