import sys
import os
from PIL import Image

# grab first and second argurment

if __name__ == '__main__':

    image_dir = f'./jpg_files/{sys.argv[1]}'
    output_dir = f'./png_files/{sys.argv[2]}'

    if os.path.exists(image_dir):

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for fname in os.listdir(image_dir):
            # convert images to pngs
            image = Image.open(f'{image_dir}/{fname}')
            clean_name = os.path.splitext(fname)[0]
            image.save(f'{output_dir}/{clean_name}.png', 'png')
            print('Done!')
    else:
        print('Can\'t find the file/directory.')
