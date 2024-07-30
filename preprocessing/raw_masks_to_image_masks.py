import os
from PIL import Image
import cv2

input_dir = '../data/data_train_competition/masks_pre/test_split'
output_dir = '../data/data_train_competition/masks_post/test_split'

# This allows for 10 persons #

palette: list[int] = [
        0, 0, 0, # For background -> Black
        255, 0, 0, # For persons -> Red
    ]

for j in os.listdir(input_dir):
    if j == '.DS_Store':
        continue
    
    image_path = os.path.join(input_dir, j)
    mask = Image.open(image_path).convert('P')
    
    # Ensure that all non-zero values are set to 1
    mask_data = mask.load()
    width, height = mask.size
    for y in range(height):
        for x in range(width):
            if mask_data[x, y] > 0:
                mask_data[x, y] = 1
    
    mask.putpalette(palette)
    save_path = os.path.join(output_dir, j)
    mask.save(save_path, 'PNG')


