import re
month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    user_date = input("Date: ")
    if " " not in user_date:
        seperated = user_date.split('/')
        print(seperated[2]+"-"+seperated[0]+"-"+seperated[1])
        break
    else:
        seperated = re.split('[," "]', user_date)
        if seperated[0] in month:
            print(seperated[-1], "-", seperated.index(seperated[0])+1, "-", seperated[1])
            print(seperated)
            break
        else:
            continue