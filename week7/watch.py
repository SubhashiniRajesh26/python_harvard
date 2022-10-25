import re
# import sys


def main():
    print(parse(input("HTML: ")))



def parse(s):
    if re.search("<iframe(.)*><\/iframe>", s):
        pattrn = re.search("(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        if pattrn:
            split_url = pattrn.groups()
            # print(split_url)
            return "https://youtu.be/" + split_url[3]
    


if __name__ == "__main__":
    main()
