# Written by Ahmad Cooper
import os
import pyperclip

def rename_files():
    # Get the folder path from the clipboard
    path = os.path.join(pyperclip.paste().strip('"'),'')
    
    # Check if the folder path exists
    if not os.path.exists(path):
        print(f"Error: The folder path '{path}' does not exist.")
        return

    # Get all the files in the folder
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
  # files = [f for f in os.listdir(path) if f.endswith((".jpg", ".jpeg", ".png"))]

    # Rename the files
    # {:04d}".format(i+1), will pad the number with leading zeros to make it 4 digits long
    for i, file in enumerate(files):
        old_file_path = os.path.join(path, file)
        new_file_name = os.path.join(path, "{:04d}{}".format(i+1, os.path.splitext(file)[1]))
        os.rename(old_file_path, new_file_name)
    print("Files have been renamed")

if __name__ == "__main__":
    rename_files()
