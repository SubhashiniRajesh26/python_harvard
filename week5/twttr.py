def main():
    str = input("Enter the String: ")
    # print(removevowel(str))
    print(shorten(str))


def shorten(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    removed = ['' if char in vowels else char for char in str]
    result = "".join(removed)
    return result

main()