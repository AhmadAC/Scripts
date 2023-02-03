# Written by Ahmad Cooper
# Google Drive Uploader
# Uploads files from a folder called "Upload". If the folder doesn't exist, it will make one
# If the files are the same filesize as the folders in Google Drive, it'll skill the upload. This is to stop uploading duplicates.


import os
import pw
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
client_secrets_file = os.path.join(script_dir, 'client_secrets.json')
settings_file = os.path.join(script_dir, 'settings.yaml')
upload_folder = os.path.join(script_dir, 'Upload')

# Connect to Google Drive
gauth = GoogleAuth()
gauth.LoadClientConfigFile(client_secrets_file)
drive = GoogleDrive(gauth)
gauth.LoadCredentialsFile(settings_file)

# Check if the "Upload" folder exists in the script directory
if not os.path.exists(upload_folder):
    os.mkdir(upload_folder)
    print("Upload folder created. Please put files to upload to google here and rerun the script.")
    exit()

# Loop through each file in the "Upload" folder
for filename in os.listdir(upload_folder):
    # Get the path of the current file
    file_path = os.path.join(upload_folder, filename)
    # Query Google Drive for a file with the same name and parent folder
    query = "title='" + filename + "' and '" + pw.folder_id + "' in parents and trashed = false"
    file_list = drive.ListFile({'q': query}).GetList()
    if len(file_list) == 0: # if no file with the same name is found
        # Create a new Google Drive file with the same name
        gfile = drive.CreateFile({'parents' : [{'id' : pw.folder_id}], 'title' : filename})
        # Set the content of the file to the contents of the current file
        gfile.SetContentFile(file_path)
        # Upload the file to the designated Google Drive folder
        gfile.Upload()
        print(f'{filename} was uploaded.')
    else:
        gfile = file_list[0]
        local_file_size = os.path.getsize(file_path)
        remote_file_size = gfile.metadata['fileSize']

        if int(local_file_size) == int(remote_file_size):
            print(f'{filename} already exists on Google Drive, skipping upload.')
        else:
            gfile.SetContentFile(file_path)
            gfile.Upload()
            print(f'{filename} was modified locally, the remote file was updated.')
