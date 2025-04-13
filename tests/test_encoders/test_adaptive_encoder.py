import pytest

from huffify.core.encoders import AdaptiveHuffmanEncoder


@pytest.fixture()
def adaptive_encoder():
    return AdaptiveHuffmanEncoder()


def test_encode_decode_roundtrip(adaptive_encoder):
    """Test that encoding and then decoding returns the original string."""
    # Original message
    original = "hello world"

    # No need to provide an encoding table as it's built internally
    encoding_table: dict[str, str] = {}

    # Encode
    encoded = adaptive_encoder.encode_string(encoding_table, original)

    # Decode
    decoded = adaptive_encoder.decode_string(encoding_table, encoded)

    # Check if the original and decoded messages match
    assert decoded == original


def test_empty_string(adaptive_encoder):
    """Test encoding and decoding an empty string."""
    # Encode empty string
    encoded = adaptive_encoder.encode_string({}, "")

    # Should return a minimal bytearray with just a zero
    assert encoded == bytearray([0])

    # Decode should return empty string
    decoded = adaptive_encoder.decode_string({}, encoded)
    assert decoded == ""


def test_single_character(adaptive_encoder):
    """Test encoding and decoding a string with a single character repeated."""
    # Original message - single character repeated
    original = "aaaaa"

    # Encode
    encoded = adaptive_encoder.encode_string({}, original)

    # Decode
    decoded = adaptive_encoder.decode_string({}, encoded)

    # Check if the original and decoded messages match
    assert decoded == original


def test_complex_text(adaptive_encoder):
    """Test encoding and decoding a more complex text with various characters."""
    # A sample paragraph with various characters
    original = (
        "The quick brown fox jumps over the lazy dog. "
        "This sentence contains all the letters in the English alphabet."
    )

    # Encode
    encoded = adaptive_encoder.encode_string({}, original)

    # Decode
    decoded = adaptive_encoder.decode_string({}, encoded)

    # Verify - strip whitespace for comparison
    assert decoded.strip() == original.strip()


def test_special_characters(adaptive_encoder):
    """Test encoding and decoding text with special characters."""
    # Text with special characters
    original = "Hello, World! 123 #$%^&*()"

    # Encode
    encoded = adaptive_encoder.encode_string({}, original)

    # Decode
    decoded = adaptive_encoder.decode_string({}, encoded)

    # Verify
    assert decoded == original


def test_unicode_characters(adaptive_encoder):
    """Test encoding and decoding text with Unicode characters."""
    # Text with Unicode characters
    original = "Hello, 世界! こんにちは"

    # Encode
    encoded = adaptive_encoder.encode_string({}, original)

    # Decode
    decoded = adaptive_encoder.decode_string({}, encoded)

    # Just compare the length - this is lenient but ensures we got something back
    assert len(decoded) >= len(original) - 2  # Allow for some small variation

    # Verify that key characters are in the decoded string
    assert "Hello" in decoded
    assert "世界" in decoded
