import torchvision.transforms as transforms
from PIL import Image
import os

# Giving the path that include our jpg files
path = './input'
jpg_list = os.listdir(path)

# Creating a new directory for resized images
saving_path = 'resized'
os.mkdir(saving_path)

# Iterate over the images's paths, resizing them and saving to new directory
for img_path in jpg_list:
    print("--------------------------------------")
    print("IMAGE " + img_path)
    img = Image.open(f"{path}/{img_path}")
    size = img.size
    print(f"Original size: {size}")
    
    # We want to get images with size 80x64
    transform = transforms.Resize(size = (64,80))
    img = transform(img)
    print("Size after resize:", img.size)
    img.save(f"./{saving_path}/{img_path}")
    print("Resized image saved.")