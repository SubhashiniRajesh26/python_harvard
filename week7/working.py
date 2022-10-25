import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    format = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A_P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A_P]M)$", s)
    if format:
        split_time = format.groups()
        # print(split_time)
        if(int(split_time[1]) > 12 or int(split_time[5]) > 12):
            raise ValueError
        first_part = format_24(split_time[1], split_time[2], split_time[3])
        sec_part = format_24(split_time[5], split_time[6], split_time[7])
        return first_part + " to " + sec_part
    else:
        raise ValueError

def format_24(hours, minute, am_pm):
    if am_pm == 'PM':
        if int(hours) == 12:
            new_hour = 12
        else:
            new_hour = int(hours) + 12
    else:
        if int(hours) == 12:
            new_hour = 0
        else:
            new_hour = int(hours)
    if minute == None:
        new_minute = ":00"
        new_time = f"{new_hour:02}" + new_minute
    else:
        new_time = f"{new_hour:02}" + ":" +minute
    return new_time



if __name__ == "__main__":
    main()
