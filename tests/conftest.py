import pytest

DUMMY_DATA = "tests/data/dummy.txt"


@pytest.fixture(scope="module")
def data_from_str():
    return "hello world"


@pytest.fixture(scope="module")
def data_from_file():
    with open(DUMMY_DATA) as data:
        return data.read().strip()
