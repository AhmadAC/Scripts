import os
import pyperclip
import zipfile

path = os.path.join(pyperclip.paste().strip('"'),'')

for file in os.scandir(path):
    if file.is_file() and file.name.endswith(".zip"):
        with zipfile.ZipFile(file, 'r') as zip_file:
            zip_file.extractall(os.path.splitext(file.path)[0])

print("Done!")
