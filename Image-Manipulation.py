##!/usr/bin/env python3
from PIL import Image
import glob

source = str(input("Enter the source directory:"))
source1 = source+"\*.jpg"
print(source1)
image_files = glob.glob(source1)

for file in image_files:
  im = Image.open(file)
  imn = im.rotate(90).resize((128,128))
  destination = "C:\\Users\\mbk7368\\Desktop\\" + file.split("/")[-1].split(".")[0] + ".jpeg"
  imn.save(destination)
