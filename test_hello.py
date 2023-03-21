from hello import hello


def test_hello():
    hello("John") == "hello, John"

def test_hello():
    assert hello("John") == "hello, John"
    assert hello() == "hello, world"