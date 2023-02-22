# Written by Ahmad Cooper
# Converts PPT to PDF, Shuffles and adds "ink" to the final PDF
# Need to copy the path of the PPT before running
import comtypes.client
import pyperclip
import time
import sys
import os
import pyperclip
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
os.chdir(current_dir)
pdf_dir = os.path.join(parent_dir, "PDF")  
sys.path.append(f"{parent_dir}/PDF")
from RandomlyAddPDF2PDF import *        
from shuffle_2_pdf import *


os.makedirs("Output", exist_ok=True)
ext = ".pptx"
ppt_path = pyperclip.paste().strip('"')
ppt_dir, ppt_file_name = os.path.split(ppt_path)
ppt_file_name, ext = os.path.splitext(ppt_file_name)
pdf = f"Output/{ppt_file_name}.pdf"

powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
powerpoint.Presentations.Open(ppt_path)
powerpoint.ActivePresentation.SaveAs(os.path.abspath(pdf), 32) # 32 is the PDF format code
powerpoint.Quit()
shuffle_pdf(pdf)
time.sleep(1)
pdf = f"Output/{ppt_file_name}_shuffled.pdf"
add_pdfs_to_pdf(pdf)
os.startfile(f"{current_dir}/Output")