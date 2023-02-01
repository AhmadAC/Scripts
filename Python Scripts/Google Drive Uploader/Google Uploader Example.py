# This script uploads lesson plans from folders with names such as: "W25 - Mon 16", and with lesson plans named: "Term 3 - K1 - W25.docx"
# The last entry in the log file will be uploaded i.e. "W25" will upload W25 docs to specific folders within the listed folder_id.
# If no log file exists, it'll make one.
# It splits the file name, and uploads it to the keyword folder i.e. "K1", from "Term 3 - K1 - W25.docx" the file is uploaded to a folder
# with "K1" in its name.

import os
import pw #pw.py stores the Google Drive folder_id
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import logging

# Very important
script_dir = os.path.dirname(os.path.abspath(__file__))
# If you don't change the directory, you can't run the script properly from a .bat file
os.chdir(script_dir)
client_secrets_file = os.path.join(script_dir, 'client_secrets.json')
settings_file = os.path.join(script_dir, 'settings.yaml')

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

# Connect to Google Drive
gauth = GoogleAuth()
gauth.LoadClientConfigFile(client_secrets_file)
drive = GoogleDrive(gauth)
gauth.LoadCredentialsFile(settings_file)


# Define the log file path
log_file = "./Log.txt"

# Check if the log file exists
if not os.path.exists(log_file):
    # Create a new log file and ask the user to input the last line
    with open(log_file, 'w') as f:
        last_line = input("Enter the last line of the log file (e.g. W27): ")
        # Converts input to uppercase letters
        last_line = last_line.upper()
        f.write(last_line)

# Open the log file and read the last line
with open(log_file, 'r') as f:
    lines = f.readlines()
    last_line = lines[-1].strip()

# Calculate the new line
new_line = last_line[0] + str(int(last_line[1:]) + 1)

# Append the new line to the log file
with open(log_file, 'a') as f:
    f.write('\n' + new_line)




# Search for the folder with the last log entry in the filename
search_dir = "."
target_folder = None
for dir in os.listdir(search_dir):
    if last_line in dir:
        target_folder = os.path.join(search_dir, dir)
        break
if target_folder is None:
    # print(f"No folder with name containing {last_line} found.")
    logger.info(f"No folder with name containing {last_line} found.")
    exit()

# Define the file extensions to be moved
extensions = [".docx", ".DOCX"]

# Copy the contents of the target folder to the upload_folder folder
# Loop through each file in the target folder
for file in os.listdir(target_folder):
    if file.endswith(tuple(extensions)):
        file_path = os.path.join(target_folder, file)
        # Extract the keyword from the filename
        keyword = file.split("-")[1].strip()
        # Query Google Drive for a folder with the same keyword in the name and inside folder_id
        query = "mimeType='application/vnd.google-apps.folder' and title contains '" + keyword + "' and '" + pw.folder_id + "' in parents and trashed = false"
        folder_list = drive.ListFile({'q': query}).GetList()
        if len(folder_list) == 0:
            logger.warning(f'No folder found with keyword "{keyword}" inside folder_id, skipping upload.')
            continue
        else:
            folder = folder_list[0]
        # Query Google Drive for a file with the same name and parent folder
        query = "title='" + file + "' and '" + folder['id'] + "' in parents and trashed = false"
        file_list = drive.ListFile({'q': query}).GetList()
        if len(file_list) == 0: # if no file with the same name is found
            # Create a new Google Drive file with the same name
            gfile = drive.CreateFile({'parents' : [{'id' : folder['id']}], 'title' : file})
            # Set the content of the file to the contents of the current file
            gfile.SetContentFile(file_path)
            # Upload the file to the designated Google Drive folder
            gfile.Upload()
            logger.info(f'{file} was uploaded to folder "{folder["title"]}".')
        else:
            gfile = file_list[0]
            local_file_size = os.path.getsize(file_path)
            remote_file_size = gfile.metadata['fileSize']

            if int(local_file_size) == int(remote_file_size):
                logger.info(f'{file} already exists on Google Drive in folder "{folder["title"]}", skipping upload.')
            else:
                gfile.SetContentFile(file_path)
                gfile.Upload()
                logger.info(f'{file} was modified locally, the remote file in folder "{folder["title"]}" was updated.')


