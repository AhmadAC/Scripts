import concurrent.futures
import os
import shutil
import sys
import pyperclip

def move_file(src_file, dst_file):
    if os.path.exists(dst_file):
        # Rename the file to keep both copies
        i = 1
        while os.path.exists(dst_file):
            name, ext = os.path.splitext(dst_file)
            dst_file = f"{name}_{i}{ext}"
            i += 1
    shutil.move(src_file, dst_file)

def main():
    # Get the folder path from the clipboard
    path = os.path.join(pyperclip.paste().strip('"'),'')
    
    
    # Check if the folder path exists
    if not os.path.exists(path):
        print(f"Error: The folder path '{path}' does not exist.")
        return
        sys.exit()
    
    file_list = []
    for subdir, dirs, files in os.walk(path):
        for file in files:
            src_file = os.path.join(subdir, file)
            dst_file = os.path.join(path, file)
            if src_file == dst_file:
                continue
            file_list.append((src_file, dst_file))
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(move_file, src_file, dst_file) for src_file, dst_file in file_list]
        for future in concurrent.futures.as_completed(futures):
            future.result()

if __name__ == "__main__":
    main()
