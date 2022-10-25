from datetime import date
import re
import sys
import inflect

p = inflect.engine()


def main():
    try:
        year, month, day = check_date(input("Date of Birth: "))
        # print(year, month, day)
    except:
        sys.exit("Invalid Date")
    dob = date(int(year), int(month), int(day))
    # print(dob)
    date_of_today = date.today()
    diff = date_of_today - dob
    print(diff)
    minutes = diff.days * 24 * 60 #365 days
    if(check_leap(int(year))):
        output_minutes = minutes
    else:
        output_minutes = minutes + (1 * 24 * 60) #leap year 366 days
    output = p.number_to_words(output_minutes, andword="")
    print(output.capitalize() + " minutes")

    


def check_date(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split('-')
        return year, month, day

def check_leap(year):
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
        return True
    else :
        return False


    

if __name__ == "__main__":
    main()
