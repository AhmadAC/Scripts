import os
import sys
import pyperclip
from PIL import Image
from fpdf import FPDF

image_exts = ("jpeg", "jpg", "png")

# Get the directory path passed as a command line argument
if len(sys.argv) > 1:
    directory = sys.argv[1]
elif pyperclip.paste():
    directory = os.path.join(pyperclip.paste().strip('"'),'')
else:
    directory = os.getcwd()
    has_pictures = any(f.endswith(image_exts) for f in os.listdir(path=directory))
    if not has_pictures:
        print(f"No image files with the extensions {image_exts} found in the current working directory.")
        sys.exit()

if not directory:
    print("Please provide a directory path as a command line argument or copy the path to your clipboard.")
    sys.exit()

# Create an instance of the PDF class
pdf = FPDF()

# Loop through all image files in the specified directory
for image in [f for f in os.listdir(path=directory) if f.endswith(image_exts)]:
    image_path = os.path.join(directory, image)
    # Open the image
    img = Image.open(image_path)
    # Add a new page
    pdf.add_page()
    # Get image dimensions
    width, height = img.size
    # Get page dimensions
    page_width, page_height = 210, 297
    # Resize the image to fit within the page size, while maintaining aspect ratio
    ratio = min(page_width/width, page_height/height)
    width, height = int(width*ratio), int(height*ratio)
    # Calculate x and y coordinates to center the image
    x = (page_width - width) / 2
    y = (page_height - height) / 2
    # Insert the image
    pdf.image(image_path, x, y, width, height)

# Create the full path of the output file
output_path = os.path.join(directory, "combined.pdf")
# Save the PDF
pdf.output(output_path, "F")
