#!/usr/bin/env python3
from PIL import Image
import glob

source = "/home/student/images/*"
image_files = glob.glob(source)

for file in image_files:
  im = Image.open(file)
  imn = im.rotate(90).resize((128,128))
  destination = "/opt/icons/" + file.split("/")[-1].split(".")[0] + ".jpeg"
  imn.save(destination)
