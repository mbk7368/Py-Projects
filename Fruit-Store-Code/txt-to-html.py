##!/usr/bin/env python3

import os

txt_file_paths = "C:\\temp1\\descriptions\\"

def transform_txt_to_html(txt_file_path, image_file_path):
    
    file_list = os.listdir(txt_file_paths)
    for filename in file_list:
    # Read the text file contents
      with open(txt_file_path, 'r') as txt_file:
        description = txt_file.read()
    # Get the image file name
    image_file_name = os.path.basename(image_file_path)
    # Create the HTML content
    html_content = f'''
        <html>
        <body>
            <h1>Description:</h1>
            <p>{description}</p>
            <img src="{image_file_name}" alt="Image">
        </body>
        </html>    '''
    # Create the HTML file path
    txt_file_name = os.path.basename(txt_file_path)
    html_file_name = os.path.splitext(txt_file_name)[0] + '.html'
    html_file_path = os.path.join('temp1', html_file_name)
    # Write the HTML content to the HTML file
    with open(html_file_path, 'w') as html_file:
        html_file.write(html_content)
    print(f'Transformed {txt_file_path} to {html_file_path} successfully.')