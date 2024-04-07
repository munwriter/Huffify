import pytest

from huffify.encoders import MVPEncoder


@pytest.fixture()
def mvp_encoder():
    return MVPEncoder()


@pytest.mark.parametrize(
    "origin_string, expectation",
    [
        ("", bytearray()),
        ("1011", bytearray((int("1011", 2),))),
        ("11110001", bytearray((int("11110001", 2),))),
    ],
)
def test_encoder_partition(
    mvp_encoder: MVPEncoder, origin_string: str, expectation: bytearray
):
    assert mvp_encoder._make_bytes_partition(origin_string) == expectation
