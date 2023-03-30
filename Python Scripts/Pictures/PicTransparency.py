# Written by Ahmad Cooper
# Set picture transparency of a PNG image or all PNG images in a folder containing images.

from PIL import Image
import sys
import os
import pyperclip

ext = [".png", ".PNG"]
# Get the image or image containing folder 
path = os.path.join(pyperclip.paste().strip('"'), '').rstrip('\\')
if len(sys.argv) > 1:
    transparency = float(sys.argv[1])
else:
    print("No transparency parameter entered.")
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

def resize_aspect_fit():
    for item in dirs:
        if item == ".DS_Store":
            continue
        if os.path.isfile(os.path.join(path, item)) and any(item.endswith(e) for e in ext):
            try:
                img = Image.open(os.path.join(path, item))
                f, e = os.path.splitext(os.path.join(path, item))
                
                # Convert the image to RGBA mode if it's not already
                if img.mode != "RGBA":
                    img = img.convert("RGBA")

                # Split the image into separate RGB and alpha channels
                r, g, b, a = img.split()

                # Set the alpha channel to x%
                alpha = a.point(lambda i: i * transparency)

                # Put the modified alpha channel back into the image
                img.putalpha(alpha)

                # Save the modified image, overwriting the original file
                img.save(f + e, "PNG", quality=100)
                
            except Exception as e:
                print(f"Error processing {item}: {e}")

resize_aspect_fit()
