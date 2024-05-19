import os
from PIL import Image
import cv2

input_dir = '../data_train_competition/masks_pre/train'
output_dir = '../data_train_competition/masks_post/train'

# This allows for 10 persons #

palette: list[int] = [
        0, 0, 0,
        255, 0, 0, # index 1 is red
        255, 255, 0, # index 2 is yellow
        255, 255, 255, # index 3 is white
        255, 0, 255, # index 4 is magenta
        0,255, 255, # index 5 is cyan
        0, 255, 0, # index 6 is green
        0, 0, 255, # index 7 is blue
        255, 165, 0, # index 8 is orange
        128, 0, 128, # index 9 is purple
        129, 69, 19, # index 10 is brown
    ]

for j in os.listdir(input_dir):
    image_path = os.path.join(input_dir, j)
    mask = Image.open(image_path).convert('P')
    mask.putpalette(palette)
    save_path = os.path.join(output_dir, j)
    mask.save(save_path, 'PNG')


