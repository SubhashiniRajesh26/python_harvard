from bank import value
def test_hello():
    assert value("hello") == "$0"
    assert value("Hello") == "$0"
    assert value("hello, welcome") == "$0"
def test_start_with_h():
    assert value("hi newman") == "$20"
    assert value("How are you") == "$20"
def test_without_h():
    assert value("welcome mr") == "$100"
    assert value("nice to meet you") == "$100"
