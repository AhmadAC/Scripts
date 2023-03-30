import pyperclip

# Retrieve the contents of the clipboard and strip new lines and commas
clipboard = pyperclip.paste().strip("\n, ")

# Check if there are commas between values
if "," in clipboard:
    # Split the list of words into keys using commas and new lines
    keys = [key.strip() for word in clipboard.split(",") for key in word.strip().split("\n")]
else:
    # Split the list of words into keys using spaces and new lines
    keys = [key.strip() for word in clipboard.split() for key in word.strip().split("\n")]

# Create a dictionary with empty string values
template = {key: "" for key in keys}

# Convert the dictionary to a string and copy it to the clipboard
final = str(template).replace("'", "\"")
pyperclip.copy(final)
