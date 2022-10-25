from seasons import check_date, check_leap

def main():
    test_check_date()
    test_check_leap()

def test_check_date():
    assert check_date("1992-06-25") == ("1992", "06", "25")
    assert check_date("june 25 1992") == None

def test_check_leap():
    assert check_leap(1970) == False
    assert check_leap(2000) == True
    assert check_leap(2020) == True
    assert check_leap(2005) == False
    assert check_leap(1992) == True