# Written by Ahmad Cooper
import os
import PyPDF2
import pyperclip

# Get  directory
directory = pyperclip.paste().strip('"')

# Iterate through all files in directory
for filename in os.listdir(directory):
    # Check if file is a PDF
    if filename.endswith('.pdf'):
        # Open PDF
        pdf_file = open(os.path.join(directory, filename), 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        # Create directory if it does not exist
        if not os.path.exists(os.path.join(directory, "text_files")):
            os.makedirs(os.path.join(directory, "text_files"))

        # Create new text file for extracted text
        text_file = open(os.path.join(directory, "text_files", filename[:-4] + '.txt'), 'w')
        # Iterate through all pages in PDF
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            # Extract text from page
            text = page.extractText()
            # Write text to text file
            text_file.write(text)
        # Close PDF and text file
        pdf_file.close()
        text_file.close()
