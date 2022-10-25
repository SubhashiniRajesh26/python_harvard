from plates import is_valid
def test_atleast_two():
    assert is_valid("AA26") == True
    assert is_valid("CS50") == True

def test_max_min_char():
    assert is_valid("AA") == True
    assert is_valid("CSFGHT") == True
    assert is_valid("ACCV1") == True

def test_spl_char():
    assert is_valid("A_A") == False
    assert is_valid("A FG") == False

def test_zero_in_frst():
    assert is_valid("CS05") == False
    assert is_valid("AA056") == False



