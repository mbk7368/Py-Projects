##! /usr/bin/env python3

import os
import requests

file_names = os.listdir("C:\\Users\\mbk73\\Desktop\\DD\\")
file_sub_path = "C:\\Users\\mbk73\\Desktop\\DD\\"
url = "http://<corpweb-external-IP>/feedback"

file_paths = []
data_dic = {}

for file_name in file_names:
    file_appending = file_sub_path+str(file_name)
    file_paths.append(file_appending)

for file_path in file_paths:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        title = lines[0]
        name = lines[1]
        date = lines[2]
        comment = lines[3]
        file_data = {'title':title, 'name':name,'date':date,'comment':comment}
        data_dic[file_path] = file_data
        response = requests.post(url, json=data_dic)

if response.status_code == 200:
    print("Data sent successfully")
else:
    print("Error sending data, status code:"+ response.status_code)