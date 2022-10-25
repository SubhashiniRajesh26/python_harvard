def main():
    str = input("Enter the String: ")
    # print(removevowel(str))
    print(shorten(str))

def removevowel(str):
    result = ""
    for s in str:
        if(s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u'):
            continue
        else:
            result += s
    return result

def shorten(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    removed = ['' if char in vowels else char for char in str]
    result = "".join(removed)
    return result

main()



