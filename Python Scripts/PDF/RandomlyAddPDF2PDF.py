# Written by Ahmad Cooper

import os
import random
from PyPDF4 import PdfFileWriter as PDFWriter, PdfFileReader as PDFReader
import pyperclip


def add_pdfs_to_pdf(template_pdf_path, pdf_folder, output_pdf_path):
    pdf_writer = PDFWriter()
    pdf_files = [file for file in os.listdir(pdf_folder) if file.endswith(".pdf")]

    template_pdf_reader = PDFReader(template_pdf_path)

    for i in range(template_pdf_reader.getNumPages()):
        page = template_pdf_reader.getPage(i)
        overlay_pdf_path = os.path.join(pdf_folder, random.choice(pdf_files))
        overlay_pdf_reader = PDFReader(overlay_pdf_path)
        overlay_page = overlay_pdf_reader.getPage(0)

        page.mergePage(overlay_page)
        pdf_writer.addPage(page)

    with open(output_pdf_path, 'wb') as out:
        pdf_writer.write(out)

def main():
    template_pdf_path = pyperclip.paste().strip('"').strip("\\")
    # Change the folder path to one on your system
    pdf_folder = os.path.expanduser('~') + r"\OneDrive\Computer Files\Programming\1.0 - MacroBook\Ink Temp"
    output_pdf_path = os.path.splitext(template_pdf_path)[0] + "_ink.pdf"

    add_pdfs_to_pdf(template_pdf_path, pdf_folder, output_pdf_path)

if __name__ == "__main__":
    main()
