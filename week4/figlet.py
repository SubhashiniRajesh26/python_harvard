from pyfiglet import Figlet
from random import choice
import sys
figlet = Figlet()
fonts = figlet.getFonts()
# figlet.setFont(font = choice(fonts))
while True:
    if(len(sys.argv) == 1):
         print(figlet.renderText(input('Input: ')))
         break

    elif ((sys.argv[1] == '-f' or sys.argv[1] == '--font')):
        if(sys.argv[2] in fonts):
            print(figlet.renderText(input('Input: ')))
        break
    else:
        sys.exit()

# print(len(sys.argv))







