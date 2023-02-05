import os
import pyperclip
import concurrent.futures

def delete_empty_folders(path):
    # Get the folder path from the clipboard
    path = os.path.join(pyperclip.paste().strip('"'),'')
    
    
    # Check if the folder path exists
    if not os.path.exists(path):
        print(f"Error: The folder path '{path}' does not exist.")
        return

    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"Deleted empty directory: {dir_path}")

if __name__ == "__main__":
    path = pyperclip.paste().strip()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(delete_empty_folders, path)
