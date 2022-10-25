import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        numbers_split = ip.split(".")
        for num in numbers_split:
            if int(num) < 0 or int(num) > 255:
                return False
        return True
    else:
        return False




if __name__ == "__main__":
    main()
