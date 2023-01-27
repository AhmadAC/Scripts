import pyperclip
import os
from PyPDF2 import PdfFileMerger

# Get the path from clipboard and strip quotation marks
path = os.path.join(pyperclip.paste().strip('"'),'')

print(f'path : {path}')
# Create a PdfFileMerger object
merger = PdfFileMerger()

# Iterate through all PDF files in the directory
for pdf in os.listdir(path):
    if pdf.endswith(".pdf"):
        print(f'pdf : {pdf}')
        merger.append(path + pdf)

# Write the combined PDF to a file
merger.write(path + "Merged.pdf")
merger.close()

print("All PDFs in the directory have been combined into a single PDF.")
