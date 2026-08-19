from app import add, multiply


def test_add():
    assert add(2, 8) == 10

def test_multiply():
    assert multiply(2, 8) == 16