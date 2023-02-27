# Written by Ahmad Cooper
# Run the script either in a Virtual Environment i.e VS Code or via a bat file; "python resize.py pixel_width,pixel_height" or "python resize.py 1920,1080"

import os
import sys
import pyperclip
import warnings
from PIL import Image, ImageOps
warnings.simplefilter('ignore', category=Warning)


# Get the image or image containing folder 
path = os.path.join(pyperclip.paste().strip('"'),'').rstrip('\\')
if len(sys.argv) > 1:
    final_size = tuple(map(int, sys.argv[1].split(",")))
else:
    print("No final size parameter entered i.e 500,700")
    sys.exit()
# Check if the clipboard contains a file path or a directory path
if os.path.isfile(path):
    # If the clipboard contains a file path, split the path to extract the directory and filename
    path, filename = os.path.split(path)
    # Only process the file in the clipboard
    dirs = [filename]
elif os.path.isdir(path):

    try:
        dirs = os.listdir(path)
    except NotADirectoryError:
        dirs = [os.path.basename(path)]
else:
    print("Clipboard does not contain a valid file or directory path.")
    sys.exit()

ext = [".png", ".jpg",".jpeg"]

def resize_aspect_fit():
    for item in dirs:
        if item == ".DS_Store":
            continue
        if os.path.isfile(os.path.join(path, item)) and any(item.endswith(e) for e in ext):
            try:
                im = Image.open(os.path.join(path, item))
                f, e = os.path.splitext(os.path.join(path, item))
                size = im.size

                # Resize the image while maintaining aspect ratio
                final_width, final_height = final_size
                im.thumbnail((final_width, final_height), Image.LANCZOS)

                # Create a new image with the final size and paste the resized image in the center
                new_im = ImageOps.pad(im, final_size, centering=(0.5, 0.5))

                # Save the resized image
                new_im.save(f + "_resized.png", "PNG", quality=100)
            except Exception as e:
                print(f"Error processing {item}: {e}")


resize_aspect_fit()
print("Done!")
