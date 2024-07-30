import os

directory = "../data/data_train_competition/labels/test_split/"

files = os.listdir(directory)

# Print the files before renaming
print("Files before renaming:")
for filename in files:
    print(filename)

# Loop through the files and rename them
for filename in files:
    old_file = os.path.join(directory, filename)
    
    # Define the new file name (modify this as per your requirement)
    new_filename = old_file.split('/')[-1].replace('_mask.', '.')
    
    # Construct the new file path
    new_file = os.path.join(directory, new_filename)
    
    # Rename the file
    os.rename(old_file, new_file)

# List all files in the directory after renaming
renamed_files = os.listdir(directory)

# Print the files after renaming
print("Files after renaming:")
for filename in renamed_files:
    print(filename)

print("Files have been renamed successfully.")