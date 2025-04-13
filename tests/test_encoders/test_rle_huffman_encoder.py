import pytest

from huffify.core.encoders import RLEHuffmanEncoder


@pytest.fixture()
def rle_encoder():
    return RLEHuffmanEncoder()


@pytest.fixture()
def rle_encoder_custom():
    # Custom encoder with different escape character and min run length
    return RLEHuffmanEncoder(escape_char="#", min_run_length=3)


def test_encode_decode_roundtrip(rle_encoder):
    """Test that encoding and then decoding returns the original string."""
    # Original message with repetitive sequences
    original = "aaaabbbbccccddddeeeeffff"

    # Encode
    encoded = rle_encoder.encode_string({}, original)

    # Decode
    decoded = rle_encoder.decode_string({}, encoded)

    # Check if the original and decoded messages match
    assert decoded == original


def test_empty_string(rle_encoder):
    """Test encoding and decoding an empty string."""
    # Encode empty string
    encoded = rle_encoder.encode_string({}, "")

    # Decode should return empty string
    decoded = rle_encoder.decode_string({}, encoded)
    assert decoded == ""


def test_no_repetition(rle_encoder):
    """Test encoding and decoding a string with no repetitive sequences."""
    # Original message with no repetition
    original = "abcdefghijklmnopqrstuvwxyz"

    # Encode
    encoded = rle_encoder.encode_string({}, original)

    # Decode
    decoded = rle_encoder.decode_string({}, encoded)

    # Check if the original and decoded messages match
    assert decoded == original


def test_mixed_content(rle_encoder):
    """Test encoding and decoding text with both repetitive and non-repetitive parts."""
    # Text with mixed content
    original = "aaaabbbcccdddeefghijkkkkkklmnooooopqrstuvwxxxxyz"

    # Encode
    encoded = rle_encoder.encode_string({}, original)

    # Decode
    decoded = rle_encoder.decode_string({}, encoded)

    # Verify
    assert decoded == original


def test_escape_character(rle_encoder):
    """Test encoding and decoding text that contains the escape character."""
    # Original with the escape character (^)
    original = "abc^^^defg^^^^^hij"

    # Encode
    encoded = rle_encoder.encode_string({}, original)

    # Decode
    decoded = rle_encoder.decode_string({}, encoded)

    # Verify
    assert decoded == original


def test_custom_parameters(rle_encoder_custom):
    """Test encoding and decoding with custom escape character and minimum run length."""
    # Original with repetitive sequences
    original = "aaabbbcccdddeee"  # Groups of 3

    # Encode with custom parameters (min_run_length=3)
    encoded = rle_encoder_custom.encode_string({}, original)

    # Decode
    decoded = rle_encoder_custom.decode_string({}, encoded)

    # Verify
    assert decoded == original

    # The encoded data should contain the custom escape character (#)
    assert encoded[0] == ord("#")


def test_run_length_encode_decode(rle_encoder):
    """Test the RLE encoding and decoding functions directly."""
    # Test various patterns
    test_cases = [
        "",  # Empty string
        "a",  # Single char
        "aaaa",  # Just enough to trigger RLE (min_run_length=4)
        "aaa",  # Not enough to trigger RLE
        "aaaaaaaa",  # Longer run
        "ababababab",  # Alternating (no runs)
        "aaaaabbbbbccccc",  # Multiple runs
    ]

    for original in test_cases:
        # Apply RLE
        rle_encoded = rle_encoder._run_length_encode(original)

        # Decode RLE
        decoded = rle_encoder._run_length_decode(rle_encoded, rle_encoder.escape_char)

        # Original should match decoded
        assert decoded == original
