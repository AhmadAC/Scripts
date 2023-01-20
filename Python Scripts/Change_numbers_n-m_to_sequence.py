#Run numbers.bat in command line with 'Run' i.e "numbers 1-30" without quotes
#Or run "numbers.bat 1-30" in script current working directory in VS Code
#pip install pyperclip
import sys, pyperclip

final = []

if len(sys.argv) >1:
    #['numbers.py', '1-30'
    numbers = (sys.argv[1:])
    for number in numbers:
        number1= number.split('-')

    x = int(number1[0])
    y = int(number1[1])
    for finalRange in range(x,y + 1, 1):
        if finalRange == (y):
            final.append(finalRange)
        else:
            final.append(finalRange)

output = ','.join(str(e) for e in final)
#output = ', '.join(str(e) for e in final) replace above line if you want ', ' separators
pyperclip.copy(output)