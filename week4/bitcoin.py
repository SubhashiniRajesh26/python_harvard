import string
import requests
import sys
try:
    if(len(sys.argv) < 2):
        print("Missing Command Line Arguments")
        sys.exit()
    elif sys.argv[1].isalpha():
        print("Command Line argument is not an number")
    elif float(sys.argv[1]):
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        dict = response.json()
        bpi = dict['bpi']
        usd = bpi['USD']
        rate = float(usd['rate_float']) * float(sys.argv[1])
        print(f"${rate:,.4f}")
    else:
        print("Command Line Argument is not a number")
        sys.exit()


except requests.RequestException:
    pass
