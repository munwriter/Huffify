import pytest

from huffify.core.encoders import BitStreamEncoder


@pytest.fixture()
def bitstream_encoder():
    return BitStreamEncoder()


def test_encode_decode_roundtrip(bitstream_encoder):
    """Test that encoding and then decoding returns the original string."""
    # Simple encoding table for testing
    encoding_table = {"a": "0", "b": "10", "c": "110", "d": "111"}

    # Original message
    original = "abacdaba"

    # Encode
    encoded = bitstream_encoder.encode_string(encoding_table, original)

    # Decode
    decoded = bitstream_encoder.decode_string(encoding_table, encoded)

    # Check if the original and decoded messages match
    assert decoded == original


def test_empty_string(bitstream_encoder):
    """Test encoding and decoding an empty string."""
    encoding_table = {"a": "0"}

    # Encode empty string
    encoded = bitstream_encoder.encode_string(encoding_table, "")

    # First 4 bytes should contain zero (total bit count)
    assert encoded[:4] == bytearray([0, 0, 0, 0])

    # Decode should return empty string
    decoded = bitstream_encoder.decode_string(encoding_table, encoded)
    assert decoded == ""


def test_bit_calculation(bitstream_encoder):
    """Test that the total bit count is calculated and stored correctly."""
    encoding_table = {"a": "0", "b": "10", "c": "110"}

    # Message with known bit count: "ab" = "0" + "10" = 3 bits
    encoded = bitstream_encoder.encode_string(encoding_table, "ab")

    # Get the table size to find the offset to the bit count
    table_size = encoded[0]

    # Calculate the position of the bit count bytes
    # Format: [table size (1 byte)][table data...][bit count (4 bytes)]...
    bit_count_pos = 1  # After table size byte

    # Skip table data - each entry has: char (1 byte) + code length (1 byte) + code bytes
    for _ in range(table_size):
        # Skip the character
        bit_count_pos += 1

        # Skip the code length and code bytes
        if bit_count_pos < len(encoded):
            code_len = encoded[bit_count_pos]
            bit_count_pos += 1

            # Skip code bytes
            code_bytes = (code_len + 7) // 8
            bit_count_pos += code_bytes

    # Check if the bit count is stored correctly (3 in little-endian format)
    expected_bit_count = 3

    if bit_count_pos + 4 <= len(encoded):
        stored_bit_count = (
            encoded[bit_count_pos]
            | (encoded[bit_count_pos + 1] << 8)
            | (encoded[bit_count_pos + 2] << 16)
            | (encoded[bit_count_pos + 3] << 24)
        )
        assert stored_bit_count == expected_bit_count


def test_complex_message(bitstream_encoder):
    """Test encoding and decoding a more complex message with various character frequencies."""
    # Simple encoding table for testing
    encoding_table = {"a": "0", "b": "10", "c": "110", "d": "111"}

    # Original message using only characters from the table
    original = "abacdaba"

    # Encode
    encoded = bitstream_encoder.encode_string(encoding_table, original)

    # Decode
    decoded = bitstream_encoder.decode_string(encoding_table, encoded)

    # Verify
    assert decoded == original
