# check all the subdirectories in Second Phase Experiments
# and make sure that there is folders, (Color Compleixty, Human Complexity, Object Complexity, Background Salience, Position Salience, Expectancy Congruency, Relevance Congruency)

import os
from PIL import Image

# Path to the directory containing the images
image_directory = 'Second Phase Experiments'

# Get a list of all subdirectories in the directory
subdirectories = [d for d in os.listdir(image_directory) if os.path.isdir(os.path.join(image_directory, d))]

# Check each subdirectory
for subdirectory in subdirectories:
    print('Checking subdirectory:', subdirectory)

    # Check for the required folders
    required_folders = ['Color Complexity', 'Human Complexity', 'Object Complexity', 'Background Salience', 'Position Salience', 'Expectancy Congruency', 'Relevance Congruency']
    for folder in required_folders:
        if not os.path.exists(os.path.join(image_directory, subdirectory, folder)):
            print('Missing folder:', folder)

    # check the images in each folder
    for folder in required_folders:
        print('Checking images in folder:', folder)
        images = [f for f in os.listdir(os.path.join(image_directory, subdirectory, folder)) if f.endswith('.jpg')]
        for image in images:
            try:
                img = Image.open(os.path.join(image_directory, subdirectory, folder, image))
                img.verify()
            except Exception as e:
                print('Error with image:', image)
                print(e)

    print('Finished checking subdirectory:', subdirectory)
    print()