# Written by Ahmad Cooper
import pyperclip
import PyPDF2
import os

# Get PDF path from clipboard
pdf_path = pyperclip.paste().strip('"')

# Open PDF
pdf_file = open(pdf_path, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
pdf_writer = PyPDF2.PdfFileWriter()

# Ask user which pages to delete
pages_to_delete = input("Enter page numbers or ranges to delete (ex: 1,3-5): ")

# Parse user input and create list of pages to delete
pages_to_delete = pages_to_delete.split(',')
pages_to_delete_list = []
for page_range in pages_to_delete:
    if '-' in page_range:
        start, end = page_range.split('-')
        pages_to_delete_list += range(int(start)-1, int(end))
    else:
        pages_to_delete_list.append(int(page_range)-1)

# Delete pages and add remaining pages to new PDF
for i in range(pdf_reader.numPages):
    if i not in pages_to_delete_list:
        pdf_writer.addPage(pdf_reader.getPage(i))

# Save new PDF
new_pdf_path = pdf_path.split('.pdf')[0] + '_edited.pdf'
new_pdf_file = open(new_pdf_path, 'wb')
pdf_writer.write(new_pdf_file)

# Close PDF files
pdf_file.close()
new_pdf_file.close()

print(f'New PDF with deleted pages saved as {new_pdf_path}')
