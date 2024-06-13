#This is a script to remove the "libpng warning: iCCP: known incorrect sRGB profile" warning
#RUN IF MESSAGE APPEARS
from PIL import Image
import os

def remove_iccp_profile(image_path):
    with Image.open(image_path) as img:
        img.save(image_path)

# Specify the directory containing your images
image_dir = 'gallery/sprites/'

# Loop through all .png files in the directory and remove the incorrect sRGB profile
for file_name in os.listdir(image_dir):
    if file_name.endswith('.png'):
        remove_iccp_profile(os.path.join(image_dir, file_name))

print("sRGB profiles removed from all images.")
