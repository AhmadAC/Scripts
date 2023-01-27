import os
import pyperclip
import comtypes.client

# Get folder path from clipboard
folder_path = os.path.join(pyperclip.paste().strip('"'),'')
os.chdir(folder_path)

# Check if folder path is valid
if os.path.isdir(folder_path):
    # Iterate through all files in the folder
    ex = [".ppt", ".pptx", ".pptm"]
    for file_name in os.listdir(folder_path):
        if file_name.endswith(tuple(ex)):
            # Open PowerPoint and export to PDF
            powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
            ppt_file = powerpoint.Presentations.Open(os.path.join(folder_path, file_name))
            pdf_file_name = os.path.splitext(file_name)[0] + ".pdf"
            ppt_file.SaveAs(os.path.join(folder_path, pdf_file_name), 32)
            ppt_file.Close()
            powerpoint.Quit()
    print("Successfully exported all PowerPoint files in the folder to PDF.")
else:
    print("Invalid folder path.")
