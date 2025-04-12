"""Command-line interface for Huffify."""

from pathlib import Path

import click

from huffify import Huffify


@click.group()
def main():
    """Huffify - Huffman compression tool."""
    pass


@main.command()
@click.argument("input_file", type=click.Path(exists=True, dir_okay=False))
@click.argument("output_file", type=click.Path(dir_okay=False))
def compress(input_file: str, output_file: str):
    """Compress a file using Huffman coding.

    INPUT_FILE: Path to the file to compress
    OUTPUT_FILE: Path where to save the compressed file
    """
    compressor = Huffify()

    # Read input file
    with open(input_file, "r") as f:
        content = f.read()

    # Compress and save
    compressor.save(output_file, content)

    # Calculate and display statistics
    original_size = Path(input_file).stat().st_size
    compressed_size = Path(output_file).stat().st_size
    ratio = 1 - (compressed_size / original_size)

    click.echo("\nCompression complete!")
    click.echo(f"Original size: {original_size / 1024:.2f} KB")
    click.echo(f"Compressed size: {compressed_size / 1024:.2f} KB")
    click.echo(f"Compression ratio: {ratio:.2%}")


@main.command()
@click.argument("input_file", type=click.Path(exists=True, dir_okay=False))
@click.argument("output_file", type=click.Path(dir_okay=False))
def decompress(input_file: str, output_file: str):
    """Decompress a Huffman-compressed file.

    INPUT_FILE: Path to the compressed file
    OUTPUT_FILE: Path where to save the decompressed file
    """
    compressor = Huffify()

    # Decompress
    content = compressor.load(input_file)

    # Save decompressed content
    with open(output_file, "w") as f:
        f.write(content)

    click.echo("\nDecompression complete!")


@main.command()
@click.argument("message")
def table(message: str):
    """Display Huffman encoding table for a message.

    MESSAGE: Text to analyze
    """
    compressor = Huffify()
    compressor.print_encoding_table(message)


if __name__ == "__main__":
    main()
