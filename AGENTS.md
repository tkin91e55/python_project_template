AGENTS — Repository Agent Guidelines

# Project Overview

  This is a simple python project that does nothing. It scaffolds with linters, type checkers, and
  formatters pre-configured. Design a dummy sizeable python project with proper structure.

  It use poetry as dependency manager

# Tech stack

  This project use Python 3.11 and poetry for dependency management.

## Development Packages

  Generate a `pyproject.toml` with the following development packages:

###  Core Linters/Formatters

  * type checker: mypy
  * linter: ruff, pylint, pre-commit
  * documentation
   * pydocstringformatter - Docstring formatting
   * sphinx
  * testing:
    * pytest - Testing framework
    * coverage - Code coverage measurement
    * tox - Virtualenv management and test automation

# Project Architecture & Structure

## Directory Layout
```
agentic_py/
├── src/                  # Source code
│   └── agentic_py/       # Main package
│       ├── __init__.py
│       ├── core/         # Core functionality
│       ├── models/       # Data models
│       ├── services/     # Business logic
│       └── utils/        # Utility functions
├── tests/                # Test files (mirrors src structure)
│   ├── unit/
│   ├── integration/
│   └── conftest.py
├── docs/                 # Documentation
│   ├── source/
│   └── build/
├── scripts/              # Build and maintenance scripts
├── .github/              # GitHub Actions workflows
├── pyproject.toml
└── README.md
```

## Module Organization
- Keep modules focused on single responsibility
- Use `__init__.py` to expose public APIs
- Organize by feature/domain, not by type
- Limit module dependencies and avoid circular imports

# Code Style Guidelines

- Follow PEP 8 for Python code style
- PEP 257 for docstrings
- Maximum line length: 89 characters
- Use type hints for all function signatures
- Write docstrings for all public modules, classes, and functions (Google style)

## Error Handling
- Use specific exception types over generic `Exception`
- Create custom exceptions in `exceptions.py` for domain errors
- Always include context in error messages
- Log exceptions with appropriate severity levels

## Testing Standards
- Aim for >80% code coverage
- Write unit tests for all business logic
- Use integration tests for external dependencies
- Follow AAA pattern (Arrange, Act, Assert)
- Use fixtures for common test data
- Mock external services and I/O operations

# Build / Lint / Test

  ## Setup
  ```bash
  poetry install              # Install dependencies
  pre-commit install          # Set up pre-commit hooks
  ```

  ## Code Quality
  ```bash
  ruff check       # Run linter
  ruff format      # Format code
  mypy             # Type checking
  ```

  ## Testing
  ```bash
  pytest           # Run tests
  coverage         # Generate coverage report
  tox              # Run tests across multiple Python versions
  ```

  ## Documentation
  ```bash
  sphinx-build     # Build documentation
  pydocstringformatter  # Format docstrings
  ```

# Development Workflow

## Branching Strategy
- `main` - Production-ready code
- `develop` - Integration branch for features
- `feature/*` - New features and enhancements
- `bugfix/*` - Bug fixes
- `hotfix/*` - Urgent production fixes

## Pull Request Process
1. Create feature branch from `develop`
2. Implement changes with tests
3. Ensure all linters and tests pass
4. Submit PR with descriptive title and summary
5. Require at least one approval before merging
6. Squash commits when merging to keep history clean

## Code Review Standards
- Check for test coverage and quality
- Verify adherence to style guidelines
- Assess performance implications
- Look for security vulnerabilities
- Ensure documentation is updated

# Environment & Configuration

## Local Development Setup
1. use `.env.example` as template to create `.env` file

## Environment Variables
- Use `.env` files for local development (never commit)
- Store secrets in environment variables, not in code
- Use `python-dotenv` or similar for loading `.env` files
- Document all required environment variables in README

## Configuration Management
- Store config in `config.py` with environment-specific overrides
- Separate config for development, testing, and production

# Security & Operations

## Security Best Practices
- Never commit secrets, API keys, or passwords
- Use `poetry audit` to scan dependencies for vulnerabilities
- Keep dependencies updated regularly
- Validate and sanitize all user inputs
- Use parameterized queries for database operations

## Logging Standards
- Use Python's `logging` module
- Configure different log levels for environments (DEBUG, INFO, WARNING, ERROR)
- Include contextual information (timestamp, module, function)
- Log to both console and files for production
- Never log sensitive information (passwords, tokens, PII)

## Performance Monitoring
- Profile code for performance bottlenecks
- Monitor memory usage in long-running processes
- Use caching appropriately
- Optimize database queries

# Project Governance

## Versioning Strategy
- Follow Semantic Versioning (MAJOR.MINOR.PATCH)
- Update version in `pyproject.toml`
- Tag releases in git: `git tag v1.0.0`

## License
- Specify license in `pyproject.toml` and LICENSE file (use MIT License)

## CI/CD
All commands are configured to run in CI/CD pipeline. Ensure all checks pass before committing.

### GitHub Actions Setup
- Create `.github/workflows/ci.yml` to run linting, testing, type checking, and documentation builds on each PR
- Configure workflow to run on `push` to `main`/`develop` and on all pull requests
- Required checks: ruff, mypy, pytest (with coverage), and sphinx build
- Set up `.github/dependabot.yml` for automated dependency updates
- Only Python 3.11 is supported in CI/CD (No matrix strategy for versions)

# Repository Rules
- Keep changes minimal and focused; add tests when changing behavior
- Require status checks to pass before merging
- Protect `main` and `develop` branches from force pushes
