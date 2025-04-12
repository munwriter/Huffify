import pytest

from huffify.heap_nodes import LexicographicNode
from huffify.huffify import HuffmanCodec

medium_length_dataset = (
    "banana",
    "apple",
    "steam",
    "elephant",
    "clock",
    "pytest",
    "yellow",
    "brown",
    "smtp",
    "cloak",
)
symbols_dataset = ("a", "1", "=", "{}", "{{{}}}}")
short_texts_dataset = (
    "The sun shines bright today.",
    "Coffee is my morning savior.",
    "Books are windows to new worlds.",
    "Music soothes the soul.",
    "Laughter is the best medicine.",
    "Dream big, work hard, stay focused.",
    "Love conquers all.",
    "Adventure awaits around every corner.",
    "Nature's beauty knows no bounds.",
    "Kindness costs nothing but means everything.",
)

medium_texts_dataset = (
    "The sun shines bright today, casting its golden rays across the sky. Birds chirp merrily as they dance in the gentle breeze.",
    "Coffee is my morning savior, awakening my senses with its rich aroma and bold flavor. It's the fuel that propels me through the day.",
    "Books are windows to new worlds, transporting us to distant lands and times. With each turn of the page, a new adventure awaits.",
    "Music soothes the soul, its melodies weaving through the fabric of our emotions. It speaks a universal language that knows no bounds.",
    "Laughter is the best medicine, lifting our spirits and bringing joy to our hearts. It's the sweet melody of happiness in our lives.",
    "Dream big, work hard, stay focused. With determination and perseverance, we can turn our dreams into reality and achieve greatness.",
    "Love conquers all, its power transcending boundaries and overcoming obstacles. It's the force that binds us together in unity and harmony.",
    "Adventure awaits around every corner, beckoning us to explore the unknown and embrace the thrill of discovery. Let's embark on a journey!",
    "Nature's beauty knows no bounds, captivating us with its breathtaking landscapes and awe-inspiring wonders. Let's cherish and protect it.",
    "Kindness costs nothing but means everything. A simple act of kindness can brighten someone's day and create a ripple effect of positivity.",
)


@pytest.fixture()
def vanilla_huffman():
    return HuffmanCodec()


@pytest.fixture()
def lexicographic_huffman():
    return HuffmanCodec(node=LexicographicNode)


@pytest.mark.parametrize("medium_len_word", medium_length_dataset)
def test_huffman_medium_len_words(vanilla_huffman: HuffmanCodec, medium_len_word: str):
    encoded_data = vanilla_huffman.encode(medium_len_word)
    assert medium_len_word == vanilla_huffman.decode(encoded_data)


@pytest.mark.parametrize("symbols", symbols_dataset)
def test_huffman_symbols(vanilla_huffman: HuffmanCodec, symbols: str):
    encoded_data = vanilla_huffman.encode(symbols)
    assert symbols == vanilla_huffman.decode(encoded_data)


@pytest.mark.parametrize("text", short_texts_dataset)
def test_huffman_short_texts(vanilla_huffman: HuffmanCodec, text: str):
    encoded_data = vanilla_huffman.encode(text)
    assert text == vanilla_huffman.decode(encoded_data)


@pytest.mark.parametrize("text", medium_texts_dataset)
def test_huffman_medium_texts(vanilla_huffman: HuffmanCodec, text: str):
    encoded_data = vanilla_huffman.encode(text)
    assert text == vanilla_huffman.decode(encoded_data)


def test_huffman_empty_word(vanilla_huffman: HuffmanCodec):
    encoded_data = vanilla_huffman.encode("")
    assert "" == vanilla_huffman.decode(encoded_data)


@pytest.mark.parametrize("text", medium_texts_dataset)
def test_lexicographic_huffman_medium_texts(lexicographic_huffman: HuffmanCodec, text: str):
    encoded_data = lexicographic_huffman.encode(text)
    assert text == lexicographic_huffman.decode(encoded_data)


@pytest.mark.parametrize("text", symbols_dataset)
def test_lexicographic_huffman_symbols(lexicographic_huffman: HuffmanCodec, text: str):
    encoded_data = lexicographic_huffman.encode(text)
    assert text == lexicographic_huffman.decode(encoded_data)
