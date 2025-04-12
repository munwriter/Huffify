# Huffify
![PyPI - Version](https://img.shields.io/pypi/v/huffify?style=for-the-badge&color=green)
![Static Badge](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![PyPI - Format](https://img.shields.io/pypi/format/huffify?style=for-the-badge)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/munwriter/Huffify/test-lint.yml?style=for-the-badge)


## Description
Huffify allows you to compress text using Huffman algorithm. Huffify focus on flexibility - you can choose various encoders, huffman tree nodes and file managers to rich the best compressing quality
> Historical note: The Huffman algorithm was developed by David A. Huffman in 1952. [Read more about David and his algorithm](https://ru.wikipedia.org/wiki/Код_Хаффмана)

## Usage
Basic usage
```python
from huffify import HuffmanCodec
from huffify.heap_nodes import Node, LexicographicNode
from huffify.encoders import MVPEncoder

# You can use LexicographicNode that provide idempotent result and another encoder.
# Now this node and encoder set as default attributes
codec = HuffmanCodec(node=Node, encoder=MVPEncoder)
message = "The sun shines bright today."

# Here is the "FinalDataSet", which can be saved as file
encoded_message = codec.encode(message)

# Also you can decode this "FinalDataSet" to get original message
decoded_message = codec.decode(encoded_message)
```
Advanced usage
```python
from huffify import Huffify
from huffify.file_manager import Picklefier

# You can pass preferred writing into file strategy
# It's only one yet and it thrown into Huffify as default strategy
file_compressor = Huffify(file_manager=Picklefier)

# You can save your compressed message into file
file_compressor.save(path="output", message="The sun shines bright today.")

# And also load and decompress it
decoded_message = file_compressor.load(path="output")

```
Watch encoding table
```python
from huffify import HuffmanCodec

codec = HuffmanCodec()
message = "The sun shines bright today."

# If you want get encoding table as dict
encoding_table = codec._get_encoding_table(message)

# Also you can print the encoding at representative view
codec.print_encoding_table(message)

```

## Installation
Using pip
```
pip install huffify
```
Using poetry
```
poetry add huffify
```

## Development Guide

### Setting Up Development Environment

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

### Project Structure

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

### Development Tools

- **Poetry**: Dependency management and packaging
- **pytest**: Testing framework
- **black**: Code formatting
- **mypy**: Static type checking
- **isort**: Import sorting
- **ruff**: Fast Python linter
- **pre-commit**: Git hooks management

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

### Creating New Components

#### Adding a New Encoder

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

#### Adding a New Node Type

1. Create a new class that inherits from `Node` in `heap_nodes.py`:
```python
from huffify.heap_nodes import Node

class YourNewNode(Node):
    def __init__(self, char: str, freq: int):
        super().__init__(char, freq)
        # Additional initialization if needed
```

2. Add corresponding tests in `tests/test_huffify_core/`

### Contributing

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

### Release Process

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md
3. Create a new git tag
4. Push changes and tag
5. GitHub Actions will automatically publish to PyPI

### Need Help?

- Open an issue for bugs or feature requests
- Check existing issues before creating a new one
- For security issues, please email directly to glebvysokov3@gmail.com
