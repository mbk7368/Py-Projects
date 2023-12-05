##! /usr/bin/env python3

import os
import requests

file_names = os.listdir("C:\\Users\\mbk73\\Desktop\\DD\\")
file_sub_path = "C:\\Users\\mbk73\\Desktop\\DD\\"
file_paths = []
data_dic = {}

for file_name in file_names:
    file_appending = file_sub_path+str(file_name)
    file_paths.append(file_appending)

for file_path in file_paths:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        print(lines)