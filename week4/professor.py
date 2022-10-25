from ast import literal_eval
import random
import string


def main():
    level = get_level()
    print(generate_integer(level))


def get_level():
    valid_inputs = (1, 2, 3)
    while True:
        try:
            level = int(input('Level: '))
            if level in valid_inputs:
                return level
                break
            else:
                continue
        except ValueError:
            continue
    # while level not in valid_inputs:
    #     level = int(input('Level: '))
    # else:
    #     number = generate_integer(level)
    


def generate_integer(level):
    count = 0
    for i in range(10):
        if(level == 1):
            x = random.randint(0, 10)
            y = random.randint(0, 10)
        elif(level == 2):
            x = random.randint(10, 100)
            y = random.randint(10, 100)
        elif(level == 3):
            x = random.randint(100, 1000)
            y = random.randint(100, 1000)
        print(x, "+", y, "=" )
        ans = int(input())
        # ans = int(input(x,"+",y,"= "))
        if(x+y == ans):
            count += 1
        else:
            print("EEE")
            for j in range(2):
                    print(x, "+", y, "=" )
                    ans = int(input())
                    if(x+y == ans):
                        count += 1
                        break
                    else:
                        print("EEE")
                        continue
            print(x,"+", y, "=", x+y)
      
            
        

    return count


# def test(number):




if __name__ == "__main__":
    main()
