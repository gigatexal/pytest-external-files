import pytest

from hashlib import sha3_512

EXPECTED_HASH = ("840006653e9ac9e95117a15c915caab"
                 "81662918e925de9e004f774ff82d707"
                 "9a40d4d27b1b372657c61d46d470304"
                 "c88c788b3a4527ad074d1dccbee5dba"
                 "a99a")


@pytest.fixture(scope="module")
def data_from_file():
    with open("tests/data/dummy.txt") as data:
        return data.read().strip()


def test_hashfunction_0():
    encoded_text = "hello world".encode()
    actual = sha3_512(encoded_text).hexdigest()
    assert actual == EXPECTED_HASH


def test_hashfunction_1(data_from_file):
    encoded_text = data_from_file.encode()
    actual = sha3_512(encoded_text).hexdigest()
    assert actual == EXPECTED_HASH
