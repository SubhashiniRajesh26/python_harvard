def main():
    while True:
        inp = input("Enter the numbers n fraction: ")
        percent_ = convert(inp)
        # print(percent_)
        print(gauge(percent_))
        



def convert(fraction):
    try:
        x, y = fraction.split('/')
        x, y = int(x), int(y)
        print(x,y)
        # if(x > y):
            # return ValueError
        percent = x/y * 100
        return percent
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError
    
       
       


def gauge(percentage):
    if(percentage <= 1.0):
        return "E"
    elif(percentage >= 99.0):
        return "F"
    else:
        return f"{percentage:.0f}%"
    


if __name__ == "__main__":
    main()
