from working import convert, format_24
import pytest

def main():
    test_format()
    test_time()
    test_hour()
    test_minute()


def test_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")  


def test_time():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'


def test_hour():
     with pytest.raises(ValueError):
        convert("9:60 AM - 9:60 PM") 



def test_minute():
     with pytest.raises(ValueError):
        convert("9 AM - 17 PM") 


if __name__ == "__main__":
    main()