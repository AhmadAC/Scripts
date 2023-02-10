# Written by Ahmad Cooper
# pip install pyperclip ; pyperclip doesn't work on Android
import pyperclip
import sys

sys.argv
# Retrieve the contents of the clipboard and strip new lines
clipboard = pyperclip.paste().strip("\n")

# List comprehension to join the list of words into a single string separated by newline characters
# type any argument after calling the file and it'll make List to CSV i.e. "python CSV_to_List 1" or if using a bat file "list 1"
if len(sys.argv) >1:
    final = ', '.join([word.strip() for word in clipboard.split("\n")])
else:
    final = '\n'.join([word.strip() for word in clipboard.split(",")])
# Copy the final string to the clipboard
pyperclip.copy(final)
