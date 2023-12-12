#!/usr/bin/env python3

import os
from datetime import date
import reports
from emails import send_email

folder_path = "supplier-data/descriptions"

def process_data(folder_path):
    fruit_data = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as file:
                lines = file.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                fruit_data.append({"name": name, "weight": weight})
    return fruit_data

def main():
    # Process the data
    data = process_data(folder_path)
    # Generate the report text
    report_text = ""
    for item in data:
        report_text += f"name: {item['name']}\nweight: {item['weight']}\n\n"
    # Generate the report
    today = date.today().strftime("%B %d, %Y")
    reports.generate_report("/tmp/processed.pdf", "Processed Update on " + today, report_text)

    sender = "automation@example.com"
    recipient = "student@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = "/tmp/processed.pdf"
    send_email(sender, recipient, subject, body, attachment_path)

if __name__ == "__main__":
    main()