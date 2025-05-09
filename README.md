# Huffify
![PyPI - Version](https://img.shields.io/pypi/v/huffify?style=for-the-badge&color=green)
![Static Badge](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![PyPI - Format](https://img.shields.io/pypi/format/huffify?style=for-the-badge)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/munwriter/Huffify/test-lint.yml?style=for-the-badge)

## Description
Huffify allows you to compress text using Huffman algorithm. Huffify focuses on flexibility - you can choose various encoders, Huffman tree nodes, and file managers to achieve the best compression quality.

> Historical note: The Huffman algorithm was developed by David A. Huffman in 1952. [Read more about David and his algorithm](https://ru.wikipedia.org/wiki/Код_Хаффмана)

## Installation

Using pip:
```bash
pip install huffify
```

Using poetry:
```bash
poetry add huffify
```

## Usage

### Command Line Interface

Huffify provides a convenient command-line interface for common operations:

```bash
# Compress a file (auto-generates filename: input_a1b2c3d4.huf)
huffify compress input.txt

# Compress with custom filename (outputs: custom_name.huf)
huffify compress input.txt --filename=custom_name

# Compress to specific directory
huffify compress input.txt /path/to/output/dir

# Decompress a file (must have .huf extension)
huffify decompress compressed.huf output.txt

# View encoding table for a text
huffify table "Hello, World!"

# Run benchmarks
huffify benchmark
```

The CLI commands in detail:

- `compress`: Compresses a text file using Huffman coding
  - Automatically generates .huf files with unique identifiers
  - Shows compression statistics including original size, compressed size, and compression ratio
  - Usage:
    - Basic: `huffify compress <input_file> [output_dir]`
    - With custom filename: `huffify compress <input_file> [output_dir] --filename=<name>`
  - Examples:
    - `huffify compress input.txt .`  → Creates `input_a1b2c3d4.huf`
    - `huffify compress input.txt . -filename=custom` → Creates `custom.huf`
    - `huffify compress input.txt /output/dir` → Creates `/output/dir/input_a1b2c3d4.huf`

- `decompress`: Decompresses a previously compressed file
  - Only accepts files with .huf extension
  - Restores the original text content
  - Usage: `huffify decompress <compressed_file.huf> <output_file>`

- `table`: Displays the Huffman encoding table for a given text
  - Shows character-to-code mappings used in compression
  - Usage: `huffify table "<text>"`

### Python API

Basic usage:
```python
from huffify import HuffmanCodec
from huffify.core.heap_nodes import Node, LexicographicNode
from huffify.core.encoders import MVPEncoder

# You can use LexicographicNode for idempotent results
codec = HuffmanCodec(node=Node, encoder=MVPEncoder)
message = "The sun shines bright today."

# Here is the "FinalDataSet", which can be saved as file
encoded_message = codec.encode(message)

# Also you can decode this "FinalDataSet" to get original message
decoded_message = codec.decode(encoded_message)
```

File operations:
```python
from huffify import Huffify
from huffify.core.file_manager import Picklefier

# Create compressor with preferred file manager
file_compressor = Huffify(file_manager=Picklefier)

# Compress and save to file
file_compressor.save(path="output.huf", message="The sun shines bright today.")

# Load and decompress from file
decoded_message = file_compressor.load(path="output.huf")
```

## Project Structure

```
Huffify/
├── src/
│   └── huffify/
│       ├── core/           # Core compression functionality
│       │   ├── codec.py    # Huffman encoding/decoding
│       │   ├── nodes.py    # Tree node implementations
│       │   ├── encoders.py # Data encoding strategies
│       │   └── file_manager.py  # File I/O operations
│       ├── presentation/   # User interfaces
│       │   ├── cli.py      # Command-line interface
│       │   └── benchmark.py # Performance testing
│       └── utils/          # Shared utilities
├── tests/                  # Test suite
├── docs/                   # Documentation
└── examples/               # Usage examples
```

## Features

- Flexible compression with customizable components:
  - Multiple node types for tree construction
  - Pluggable encoders for different encoding strategies
  - Extensible file manager system
- Command-line interface for common operations
- Comprehensive benchmarking suite
- Type hints and documentation
- Extensive test coverage

## Contributing

We welcome contributions! Please check out our [Contributing Guide](CONTRIBUTING.md) for guidelines on how to proceed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
