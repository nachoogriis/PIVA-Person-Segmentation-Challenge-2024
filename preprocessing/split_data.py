import os
import shutil
import random

# Define paths
base_dir = '../data/data_train_competition_raw'
images_dir = os.path.join(base_dir, 'images', 'train')
masks_dir = os.path.join(base_dir, 'masks_pre', 'train')

# Define destination directories
train_images_dir = os.path.join(base_dir, 'images', 'train_split')
val_images_dir = os.path.join(base_dir, 'images', 'val_split')
test_images_dir = os.path.join(base_dir, 'images', 'test_split')

train_masks_dir = os.path.join(base_dir, 'masks_pre', 'train_split')
val_masks_dir = os.path.join(base_dir, 'masks_pre', 'val_split')
test_masks_dir = os.path.join(base_dir, 'masks_pre', 'test_split')

# Create destination directories if they don't exist
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(test_images_dir, exist_ok=True)

os.makedirs(train_masks_dir, exist_ok=True)
os.makedirs(val_masks_dir, exist_ok=True)
os.makedirs(test_masks_dir, exist_ok=True)

# List all samples
samples = os.listdir(images_dir)

# Shuffle the samples
random.shuffle(samples)

# Define split ratios
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Calculate split indices
num_samples = len(samples)
train_end = int(train_ratio * num_samples)
val_end = train_end + int(val_ratio * num_samples)

# Split samples
train_samples = samples[:train_end]
val_samples = samples[train_end:val_end]
test_samples = samples[val_end:]

def copy_files(sample_list, src_images_dir, src_masks_dir, dest_images_dir, dest_masks_dir):
    for sample in sample_list:
        # Copy image file
        src_image_path = os.path.join(src_images_dir, sample)
        dest_image_path = os.path.join(dest_images_dir, sample)
        shutil.copyfile(src_image_path, dest_image_path)

        # Copy mask file (assuming the mask file has the same name as the image file)
        sample_mask = sample.replace('jpg', 'png')
        
        src_mask_path = os.path.join(src_masks_dir, sample_mask)
        dest_mask_path = os.path.join(dest_masks_dir, sample_mask)
        shutil.copyfile(src_mask_path, dest_mask_path)

# Copy files to respective directories
copy_files(train_samples, images_dir, masks_dir, train_images_dir, train_masks_dir)
copy_files(val_samples, images_dir, masks_dir, val_images_dir, val_masks_dir)
copy_files(test_samples, images_dir, masks_dir, test_images_dir, test_masks_dir)

print("Dataset split into train, validation, and test sets successfully.")
