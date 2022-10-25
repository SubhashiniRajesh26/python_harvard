def main():
    str = input("Enter the word in camelCase: ")
    output = to_snake(str)
    if(output == -1):
        print("Enter the camel case")
    else:
        print(output)

def to_snake(str):
    result = ""
    for i in range(len(str)):
        if(str[0].isupper):
            return -1
        if (str[i].isupper()):
            result = result + '_' + str[i].lower()
        else:
            result += str[i]
    return result

main()