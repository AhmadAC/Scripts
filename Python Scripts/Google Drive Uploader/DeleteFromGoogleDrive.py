# Written by Ahmad Cooper
# Google Drive File Deleter
# Type numbers 1,2,3 ... 1-6 etc. to delete multiple files

import pw
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

# Connect to Google Drive
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# Get the list of files in the folder
file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(pw.folder_id)}).GetList()

while True:
    # Print the list of files with numbers
    for i, item in enumerate(file_list):
        print(f"{i+1}. {item['title']}")
    # Ask the user to choose one or more files to delete
    choice = input("Enter the numbers of the files to delete (or 'x' to exit): ")
    if choice.lower() == 'x':
        break
    else:
        try:
            # Parse the user's choice and build a list of file indices
            file_indices = []
            for part in choice.split(','):
                if '-' in part:
                    start, end = map(int, part.split('-'))
                    file_indices.extend(range(start-1, end))
                else:
                    file_indices.append(int(part)-1)
            # Delete the chosen files
            for i in file_indices:
                file_id = file_list[i]['id']
                drive.auth.service.files().delete(fileId=file_id).execute()
            # Update the file list
            file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(pw.folder_id)}).GetList()
            logger.info("File(s) deleted.")
        except (ValueError, IndexError):
            logger.info("Invalid choice. Please enter valid numbers or ranges of numbers.")
