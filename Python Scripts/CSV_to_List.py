import pyperclip
#create an empty list to put values in
final = [] 
#set clipboard as list
list = pyperclip.paste()
#split clipboard by ',' , to get each word
final = list.split(',')
#clean words just incase user copied: 1,2 ,3  ,4 etc
final = [_.strip(' ') for _ in final]
#join all words into a single string, each word on a new line
final = '\n'.join(final)
#copy the words to clipboard
pyperclip.copy(final)
