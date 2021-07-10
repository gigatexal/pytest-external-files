import pytest

from src.hashing import hash_value

DUMMY_DATA = "tests/data/dummy.txt"
EXPECTED_HASH = ("840006653e9ac9e95117a15c915caab"
                 "81662918e925de9e004f774ff82d707"
                 "9a40d4d27b1b372657c61d46d470304"
                 "c88c788b3a4527ad074d1dccbee5dba"
                 "a99a")


@pytest.fixture(scope="module")
def data_from_file():
    with open(DUMMY_DATA) as data:
        return data.read().strip()


def test_hashfunction_str():
    assert hash_value("hello world") == EXPECTED_HASH


def test_hashfunction_file(data_from_file):
    assert hash_value(data_from_file) == EXPECTED_HASH
