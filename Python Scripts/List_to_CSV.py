# Written by Ahmad Cooper
# pip install pyperclip ; pyperclip doesn't work on Android
import pyperclip

# Retrieve the contents of the clipboard and strip new lines
clipboard = pyperclip.paste().strip("\n")

# List comprehension to join the list of words into a single string separated by newline characters
final = ', '.join([word.strip() for word in clipboard.split("\n")])

# Copy the final string to the clipboard
pyperclip.copy(final)
