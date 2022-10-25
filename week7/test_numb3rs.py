from numb3rs import validate


def main():
    test_format()
    test_range()

def test_format():
    assert validate('10.23.45.255') == True
    assert validate('10.23.45') == False
    assert validate('10.23.') == False
    assert validate('10') == False

def test_range():
    assert validate('255.255.255.255') == True
    assert validate('300.255.255.255') == False
    assert validate('255.300.255.255') == False
    assert validate('255.255.300.255') == False