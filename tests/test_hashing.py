import pytest

from hashlib import sha3_512

def test_hashfunction_0():
    d = 'hello world'
    assert sha3_512(d.encode()).hexdigest() == '840006653e9ac9e95117a15c915caab81662918e925de9e004f774ff82d7079a40d4d27b1b372657c61d46d470304c88c788b3a4527ad074d1dccbee5dbaa99a'

def test_hashfunction_1():
    with open('tests/data/dummy.txt') as data:
        d = data.read().strip() # text should be 'hello world'
        assert sha3_512(d.encode()).hexdigest() == '840006653e9ac9e95117a15c915caab81662918e925de9e004f774ff82d7079a40d4d27b1b372657c61d46d470304c88c788b3a4527ad074d1dccbee5dbaa99a'

