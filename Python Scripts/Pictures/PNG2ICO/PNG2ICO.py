import os
from PIL import Image

def convert_all_pngs_to_ico():
    for filename in os.listdir():
        if filename.endswith('.png'):
            img = Image.open(filename)
            ico_file = os.path.splitext(filename)[0] + '.ico'
            img.save(ico_file, format='ICO')
            print(f'{filename} has been converted to {ico_file}')

convert_all_pngs_to_ico()
