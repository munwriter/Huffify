# Contributing to Huffify

Thank you for your interest in contributing to Huffify! This document provides guidelines and instructions for contributing to the project.

## Setting Up Development Environment

1. Clone the repository
```bash
git clone https://github.com/munwriter/Huffify.git
cd Huffify
```

2. Install Poetry (if not already installed)
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies
```bash
poetry install
```

4. Install pre-commit hooks
```bash
make setup-pre-commit
```

## Project Structure

```
Huffify/
├── src/huffify/          # Main package directory
│   ├── __init__.py      # Package initialization
│   ├── abstract.py      # Abstract base classes
│   ├── annotations.py   # Type annotations
│   ├── encoders.py      # Encoding implementations
│   ├── file_manger.py   # File handling utilities
│   ├── heap_nodes.py    # Huffman tree node implementations
│   └── huffify.py       # Core compression logic
├── tests/               # Test directory
│   ├── test_huffify_core/  # Core functionality tests
│   └── test_encoders/      # Encoder-specific tests
├── .github/             # GitHub Actions workflows
├── poetry.lock         # Lock file for dependencies
├── pyproject.toml      # Project configuration
└── .pre-commit-config.yaml  # Pre-commit hooks configuration
```

## Development Tools

- **Poetry**: Dependency management and packaging
- **pytest**: Testing framework
- **black**: Code formatting
- **mypy**: Static type checking
- **isort**: Import sorting
- **ruff**: Fast Python linter
- **pre-commit**: Git hooks management

## Development Commands

### Running Tests

```bash
# Run all tests
make tests

# Run tests with coverage report
make coverage
```

### Code Quality Checks

```bash
# Run all checks (format + lint)
make check-all

# Format code
make format

# Lint code
make lint

# Run all checks and tests
make prepare
```

## Creating New Components

### Adding a New Encoder

1. Create a new class that inherits from `IEncoder` in `encoders.py`:
```python
from huffify.abstract import IEncoder

class YourNewEncoder(IEncoder):
    def encode(self, data: str) -> bytes:
        # Your encoding implementation
        pass

    def decode(self, data: bytes) -> str:
        # Your decoding implementation
        pass
```

2. Add corresponding tests in `tests/test_encoders/`

### Adding a New Node Type

1. Create a new class that inherits from `Node` in `heap_nodes.py`:
```python
from huffify.heap_nodes import Node

class YourNewNode(Node):
    def __init__(self, char: str, freq: int):
        super().__init__(char, freq)
        # Additional initialization if needed
```

2. Add corresponding tests in `tests/test_huffify_core/`

## Contributing Process

1. Fork the repository
2. Create a new branch for your feature
```bash
git checkout -b feature/your-feature-name
```
3. Make your changes
4. Run tests and code quality checks
5. Commit your changes using conventional commits
```bash
git commit -m "feat: add new encoder implementation"
```
6. Push to your fork and create a Pull Request

## Release Process

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md
3. Create a new git tag
4. Push changes and tag
5. GitHub Actions will automatically publish to PyPI

## Getting Help

- Open an issue for bugs or feature requests
- Check existing issues before creating a new one
- For security issues, please email directly to glebvysokov3@gmail.com
