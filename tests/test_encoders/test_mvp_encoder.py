import pytest

from huffify.core.encoders import MVPEncoder


@pytest.fixture()
def mvp_encoder():
    return MVPEncoder()


@pytest.mark.parametrize(
    "origin_string, expectation",
    [
        ("", bytearray((0,))),
        ("1011", bytearray((4, int("1011", 2)))),
        ("11110001", bytearray((0, int("11110001", 2)))),
    ],
)
def test_encoder_partition(
    mvp_encoder: MVPEncoder, origin_string: str, expectation: bytearray
):
    assert mvp_encoder._make_bytes_partition(origin_string) == expectation
