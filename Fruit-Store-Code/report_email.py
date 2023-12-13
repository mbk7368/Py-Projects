#!/usr/bin/env python3

import os
from datetime import date
from reports import generate_report

folder_path = "/home/student/supplier-data/descriptions"

def process_data(folder_path):
    fruit_data = []
    output = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as file:
                lines = file.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                fruit_data.append({"name": name, "weight": weight})
    for item in fruit_data:
        output += "\n\n"
        output += f"name: {item['name']}\n"
        output += f"weight: {item['weight']}\n"
        output += "\n"
    return output

def main():
    generate_report("/tmp/processed.pdf")
    sender = "automation@example.com"
    recipient = "student@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = "/tmp/processed.pdf"
    send_email(sender, recipient, subject, body, attachment_path)

if __name__ == "__main__":
    main()