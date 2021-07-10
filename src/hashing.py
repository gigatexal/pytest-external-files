from hashlib import sha3_512


def hash_value(text):
    return sha3_512(
        text.encode()).hexdigest()
