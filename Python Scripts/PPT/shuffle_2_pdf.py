import pyperclip
import PyPDF2
import random
import os

def shuffle_pdf():
    pdf_path = pyperclip.paste().strip('"')
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    num_pages = pdf_reader.getNumPages()
    page_indices = list(range(num_pages))
    random.shuffle(page_indices)
    pdf_writer = PyPDF2.PdfFileWriter()
    for index in page_indices:
        pdf_writer.addPage(pdf_reader.getPage(index))
    pdf_dir, pdf_file_name = os.path.split(pdf_path)
    pdf_file_name, pdf_ext = os.path.splitext(pdf_file_name)
    new_pdf_file_name = pdf_file_name + "_shuffled" + pdf_ext
    new_pdf_path = os.path.join(pdf_dir, new_pdf_file_name)
    shuffled_pdf = open(new_pdf_path, 'wb')
    pdf_writer.write(shuffled_pdf)
    shuffled_pdf.close()
    pdf_file.close()
    return pdf_file_name

