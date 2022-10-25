from curses.ascii import isalpha


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if(len(s) < 2 or len(s) > 6):
        return False
    if(s[0].isdigit() or s[-1].isalpha()):
        return False
    if(s[0].isalpha() and s[1].isalpha):
        return True
    else:
        return True
    


main()
