def main():
    exp = input("Enter the expression with space: ")
    x, y, z = exp.split(" ")
    result = calc(x,y,z)
    if(result == -1 ):
        print("enter the valid number")
    else:
        print(f'{result:.1f}')

def calc(x, y, z):
    if(x.isalpha() or z.isalpha()):
        return -1
    elif(y == '+'):
        return float(x) + float(z)
    elif(y == '-'):
        return float(x) - float(z)
    elif(y == '*'):
        return float(x) * float(z)
    elif(y == '/'):
        if(z == '0'):
            return -1
        else:
            return float(x) / float(z)

main()