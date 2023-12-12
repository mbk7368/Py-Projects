#!/usr/bin/env python3

import requests
import os

# This example shows how multiple files can be uploaded using
# the Python Requests module

url = "http://localhost/upload/"
directory = "/path/to/images/"

# Get the list of files in the directory
file_list = os.listdir(directory)

for filename in file_list:
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Construct the file path
        image_path = os.path.join(directory, filename)

        with open(image_path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})

            # Check if the request was successful
            if r.status_code == 201:
                print(f"Image {filename} uploaded successfully.")
            else:
                print(f"Failed to upload image {filename}. Error code: {r.status_code}")
    else:
        print(f"Skipped file {filename} as it is not a supported image format.")