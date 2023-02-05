# Written by Ahmad Cooper
# If you have SECURED your PDF from editing and forget your password. This may help to unlock it.
# For educational purposes only. Use at your own risk.
# Copy the path to the folder or put the script in the folder with the PDFs
import os
import PyPDF2
import pyperclip


if pyperclip.paste():
    directory = os.path.join(pyperclip.paste().strip('"'),'')
else:
    directory = os.getcwd()

for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'rb') as file:
            pdf = PyPDF2.PdfFileReader(file)
            if pdf.isEncrypted:
                unlocked_filepath = os.path.join(directory, filename[:-4] + "_unlocked.pdf")
                with open(unlocked_filepath, 'wb') as output:
                    writer = PyPDF2.PdfFileWriter()
                    writer.appendPagesFromReader(pdf)
                    writer.write(output)
                    print(f"{filename} unlocked and saved as {unlocked_filepath}")
                file.close()    
                os.remove(filepath) #can comment this out to keep the original file