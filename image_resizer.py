import os
from PIL import Image

# Path to the directory containing the images
image_directory = 'images/cocacola'

# Target dimensions for resizing
target_width = 1200
target_height = 1600

# Get a list of all files in the directory
files = os.listdir(image_directory)

# Filter out files that are not images (you can adjust this filter based on your needs)
image_files = [f for f in files if f.endswith(('.png', '.jpg', '.jpeg'))]

# Sort the files to ensure sequential renaming
image_files.sort()

# Rename and resize the images
for idx, filename in enumerate(image_files):
    # Define the new filename
    new_filename = f"{idx + 1}.png"
    
    # Define the full paths
    old_path = os.path.join(image_directory, filename)
    new_path = os.path.join(image_directory, new_filename)
    
    # Open the image file
    with Image.open(old_path) as img:
        # Resize the image
        img = img.resize((target_width, target_height), Image.ANTIALIAS)
        # Save the resized image with the new filename
        img.save(new_path)

    # Remove the old file if the filename has changed
    if old_path != new_path:
        os.remove(old_path)

print("Image renaming and resizing completed.")
