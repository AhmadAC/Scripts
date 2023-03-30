import os
import pyperclip
import zipfile

path = os.path.join(pyperclip.paste().strip('"'),'')

for file in path.iterdir():
        if file.suffix == ".zip":
            with zipfile.ZipFile(file, 'r') as zip_file:
                zip_file.extractall(file.with_suffix(''))

print("Done!")