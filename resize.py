import os
from PIL import Image

# Set the directory path
directory = "F:/cache"

# Set the new size
new_size = (1024, 1024)

# Loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Open the image
        img = Image.open(os.path.join(directory, filename))

        # Resize the image
        img = img.resize(new_size)

        # Save the image with the same filename
        img.save(os.path.join(directory, filename))
