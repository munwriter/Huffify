import pytest

from huffify.huffify import HuffmanCodec


@pytest.fixture()
def vanilla_huffman():
    return HuffmanCodec()


def test_core(vanilla_huffman: HuffmanCodec):
    encoded_data = vanilla_huffman.encode("banana")
    assert "banana" == vanilla_huffman.decode(encoded_data)
