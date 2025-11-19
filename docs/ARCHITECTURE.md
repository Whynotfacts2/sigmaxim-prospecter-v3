# Project Architecture

## Overview

SigmaXim Prospecter V3 is built with a modular, layered architecture designed for maintainability, extensibility, and AI platform compatibility.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                     Application Layer                    │
│                    (CLI / API / UI)                      │
└─────────────────────────────────────────────────────────┘
                            │
┌─────────────────────────────────────────────────────────┐
│                      Core Layer                          │
│              (Business Logic & Orchestration)            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Prospecter  │  │ Lead Scoring │  │  Analytics   │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                            │
┌─────────────────────────────────────────────────────────┐
│                    Services Layer                        │
│           (External Integrations & APIs)                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  AI Service  │  │ CRM Service  │  │ Data Service │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                            │
┌─────────────────────────────────────────────────────────┐
│                   Utilities Layer                        │
│        (Common Functions & Infrastructure)               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Logging    │  │  Validation  │  │   Helpers    │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
```

## Design Principles

### 1. Separation of Concerns
Each layer has a specific responsibility:
- **Core**: Business logic and domain models
- **Services**: External integrations and I/O operations
- **Utils**: Reusable utility functions
- **Config**: Configuration management

### 2. Dependency Injection
Components receive their dependencies through constructors, making them easier to test and more flexible.

### 3. Interface-Based Design
Services implement clear interfaces, allowing for easy substitution and testing with mocks.

### 4. Type Safety
Extensive use of type hints throughout the codebase ensures type safety and better IDE support.

### 5. Configuration-Driven
All configurable values are externalized through environment variables and settings.

## Core Components

### Prospecter
The main orchestrator that coordinates the prospecting workflow:
- Lead intake and validation
- AI-powered scoring
- Result filtering and ranking
- Workflow management

### Lead Model
Represents a prospect/lead with all relevant data:
- Contact information
- Company details
- Engagement history
- Calculated scores

### AIService
Unified interface for AI platform integrations:
- Supports multiple providers (Google AI, OpenAI, Anthropic)
- Consistent API across providers
- Graceful error handling
- Rate limiting and retry logic

## Data Flow

```
1. Input → Lead Creation
2. Lead → Validation
3. Lead → AI Analysis (via AIService)
4. AI Results → Score Calculation
5. Scored Leads → Filtering
6. Filtered Results → Output
```

## AI Platform Compatibility

### Design for AI Understanding
The codebase is structured to be easily understood by AI assistants:

1. **Clear Naming**: Descriptive names for all components
2. **Comprehensive Docstrings**: Every module, class, and function documented
3. **Type Hints**: Complete type annotations
4. **Modular Structure**: Logical organization of code
5. **Comments**: Complex logic is explained

### Platform-Specific Files
- `.cursorrules`: Guidelines for Cursor AI
- `.aidigestignore`: Files to exclude from AI context
- `.editorconfig`: Consistent formatting across editors

## Testing Strategy

### Unit Tests
- Test individual functions and classes in isolation
- Mock external dependencies
- Focus on business logic correctness

### Integration Tests
- Test component interactions
- Use test databases/services
- Verify end-to-end workflows

### Test Organization
```
tests/
├── unit/              # Isolated component tests
│   ├── test_prospecter.py
│   ├── test_settings.py
│   └── test_utils.py
└── integration/       # Component interaction tests
    └── test_workflow.py
```

## Security Architecture

### Defense in Depth
1. **Input Validation**: All user input is validated and sanitized
2. **API Key Management**: Secrets stored in environment variables
3. **Least Privilege**: Components have minimal required permissions
4. **Error Handling**: No sensitive data in error messages

### Secure Configuration
- No hardcoded secrets
- Environment-based configuration
- .env files excluded from version control

## Scalability Considerations

### Current State
- Single-process execution
- In-memory data processing
- Local file storage

### Future Enhancements
- Async/await for concurrent operations
- Database integration for persistence
- Queue-based processing for high volume
- Distributed processing support

## Error Handling

### Hierarchical Error Management
1. **Service Layer**: Catch and log external service errors
2. **Core Layer**: Handle business logic errors
3. **Application Layer**: Present user-friendly error messages

### Logging Strategy
- Structured logging with levels (DEBUG, INFO, WARNING, ERROR)
- Contextual information in logs
- Separate logs for different components

## Extension Points

The architecture is designed to be easily extended:

1. **New AI Providers**: Implement AIProvider interface
2. **New Lead Sources**: Add new service integrations
3. **Custom Scoring**: Extend scoring algorithms
4. **Additional Integrations**: Add to services layer

## Performance Considerations

### Current Optimizations
- Cached configuration loading
- Lazy initialization where appropriate
- Efficient data structures

### Future Optimizations
- Batch processing for leads
- Caching of AI responses
- Database query optimization
- Connection pooling

## Technology Stack

- **Language**: Python 3.9+
- **Configuration**: Pydantic Settings
- **Testing**: pytest
- **Code Quality**: ruff, mypy, black
- **Documentation**: Docstrings (Google style)

## Best Practices

1. **Code Style**: Follow PEP 8
2. **Documentation**: Maintain comprehensive docs
3. **Testing**: Write tests for new features
4. **Version Control**: Meaningful commit messages
5. **Security**: Regular dependency updates
