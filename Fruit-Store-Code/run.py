#!/usr/bin/env python3

import os
import requests
import json

# Configuration
description_directory = "/home/student/supplier-data/descriptions"
image_directory = "/home/student/supplier-data/images"
url = "http://34.148.143.46/fruits"

def process_text_files(description_directory, image_directory, url):
    # Get the list of text files in the description directory
    file_list = os.listdir(description_directory)

    for filename in file_list:
        if filename.endswith('.txt'):
            # Construct the file paths for processing
            text_file_path = os.path.join(description_directory, filename)
            image_name = os.path.splitext(filename)[0] + ".jpeg"
            image_path = os.path.join(image_directory, image_name)

            # Read the text file
            with open(text_file_path, 'r') as file:
                lines = file.readlines()
                name = lines[0].strip()
                weight = int(lines[1].strip().split()[0])
                description = lines[2].strip()

            # Create the JSON dictionary
            fruit_data = {
                "name": name,
                "weight": weight,
                "description": description,
                "image_name": image_name
            }

            # Upload the data as JSON
            response = requests.post(url, json=fruit_data)

            # Check if the request was successful
            if response.status_code == 201:
                print(f"Data from {filename} uploaded successfully.")
            else:
                print(f"Failed to upload data from {filename}. Error code: {response.status_code}")

            # Upload the associated image
            with open(image_path, 'rb') as image_file:
                image_response = requests.post(url, files={"file": image_file})

                # Check if the request was successful
                if image_response.status_code == 201:
                    print(f"Image {image_name} uploaded successfully.")
                else:
                    print(f"Failed to upload image {image_name}. Error code: {image_response.status_code}")

# Example usage
process_text_files(description_directory, image_directory, url)