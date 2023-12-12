#!/usr/bin/env python3

from PIL import Image
import os

def process_images(directory):
    # Get the list of files in the directory
    file_list = os.listdir(directory)

    for filename in file_list:
        if filename.endswith('.tiff'):
            # Construct the file paths for processing
            image_path = os.path.join(directory, filename)
            output_filename = os.path.splitext(filename)[0] + '.jpeg'
            output_path = os.path.join(directory, output_filename)

            # Open the image
            image = Image.open(image_path)

            # Convert RGBA to RGB if necessary
            if image.mode == 'RGBA':
                image = image.convert('RGB')

            # Resize the image
            resized_image = image.resize((600, 400))

            # Save the processed image as JPEG
            resized_image.save(output_path, 'JPEG')
            print(f"Image processed and saved as: {output_path}")

# Example usage
directory = '~/supplier-data/images'
process_images(directory)