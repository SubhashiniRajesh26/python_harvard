def main():
    fuel_percentage()


def fuel_percentage():
    while True:
        try:
            inp = input("Enter the numbers n fraction: ")
            x, y = inp.split('/')
            x, y = int(x), int(y)
            if(x > y):
                raise ValueError
            percentage = x/y * 100
            if(percentage <= 1.0):
                print("E")
            elif(percentage >= 99.0):
                print("F")
            else:
                print(f"{percentage:.0f}%")
            break   

        except ValueError:
            pass
        except ZeroDivisionError:
            pass



main()