def main():
    time = input("Enter the time in minimutes and hours: ")
    convertedTime = convert(time)
    display(convertedTime)


def convert(time):
    hours, minutes = time.split(':')
    return round(int(hours) + int(minutes) / 60)

def display(time):
    if(time == 1):
        print("Lunch Time")
    if(time >= 7 and time <= 8):
        print("BreakFast Time")
    elif(time >= 12 and time <= 13):
        print("Lunch Time")
    elif(time >= 18 and time <= 19 or time >= 6 and time <= 7):
        print("Dinner Time")
    else:
        print(" ")

if __name__ == "__main__":
    main()
