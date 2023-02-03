# Written by Ahmad Cooper
# Photo renamer - renames photos with the following file extensions: ".jpg", ".jpeg", ".png". Can add more to line 18 if you want

import os
import pyperclip

def rename_files():
    # Get the folder path from the clipboard
    path = os.path.join(pyperclip.paste().strip('"'),'')
    
    
    # Check if the folder path exists
    if not os.path.exists(path):
        print(f"Error: The folder path '{path}' does not exist.")
        return

    # Get all the picture files in the folder
    picture_files = [f for f in os.listdir(path) if f.endswith((".jpg", ".jpeg", ".png"))]

    # Rename the picture files
    # {:04d}".format(i+1), will pad the number with leading zeros to make it 4 digits long
    for i, picture_file in enumerate(picture_files):
        old_file_path = os.path.join(path, picture_file)
        #new_file_name = "{:04d}{}".format(i+1, os.path.splitext(picture_file)[1])
        new_file_name = os.path.join(path, "{:04d}{}".format(i+1, os.path.splitext(picture_file)[1]))
        os.rename(old_file_path, new_file_name)
        print("Photos have been renamed")

if __name__ == "__main__":
    rename_files()