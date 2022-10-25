from um import count

def main():
    test_cases()
    test_with_words()

def test_cases():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_with_words():
    assert count("Yummy") == 0
    assert count("... um ... ") == 1
    assert count(" hello um welcome") == 1

if __name__ == "__main__":
    main()

