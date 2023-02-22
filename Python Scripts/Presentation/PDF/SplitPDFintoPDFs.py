# Written by Ahmad Cooper

import PyPDF2
import os
import pyperclip

def split_pdf(path):
    pdf = PyPDF2.PdfFileReader(path)
    base_path, ext = os.path.splitext(path)
    folder_path = os.path.dirname(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        # Uncomment if you want to have the basefile name included in the split files
        # new_path = f"{base_path} {page+1}{ext}"
        new_path = f"{folder_path}/{page+1}{ext}"
        with open(new_path, "wb") as f:
            pdf_writer.write(f)

if __name__ == "__main__":
    path = pyperclip.paste().strip('"').strip("\\")
    split_pdf(path)
