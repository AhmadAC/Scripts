import pathlib
import pyperclip
import zipfile

path = pathlib.Path(pyperclip.paste())

for file in path.iterdir():
        if file.suffix == ".zip":
            with zipfile.ZipFile(file, 'r') as zip_file:
                zip_file.extractall(file.with_suffix(''))

print("Done!")