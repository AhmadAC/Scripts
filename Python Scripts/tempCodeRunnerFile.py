import pathlib
import pyperclip
import zipfile
import subprocess

path = pathlib.Path(pyperclip.paste())

for file in path.iterdir():
    try:
        if file.suffix == ".zip":
            with zipfile.ZipFile(file, 'r') as zip_file:
                zip_file.extractall(file.with_suffix(''))
        elif file.suffix == ".rar":
            subprocess.run(["winrar", "x", file, file.with_suffix('')], check=True)
    except (zipfile.BadZipFile, subprocess.CalledProcessError) as e:
        print(f"Error extracting {file}: {e}")
