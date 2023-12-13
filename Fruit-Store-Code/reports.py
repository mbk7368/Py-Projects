#!/usr/bin/env python3

import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date

folder_path = "/home/student/supplier-data/descriptions"

def read_text_files(folder_path):
    data = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as file:
                name = file.readline().strip()  # Read the first line as the name
                weight = file.readline().strip()  # Read the second line as the weight
                description = file.read().strip()  # Read the rest as the description

                data.append({"name": name, "weight": weight, "description": description})
    return data

def generate_report(filename):
    data = read_text_files(folder_path)
    today = date.today().strftime("%B %d, %Y")
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_content = []
    report_title = Paragraph(f"Processed Update on {today}", styles["h1"])
    report_content.append(report_title)
    report_content.append(Spacer(1, 12))  # Add blank line

    for item in data:
        name = item["name"]
        weight = item["weight"]
        description = item["description"]
        report_content.append(Paragraph(f"name: {name}", styles["BodyText"]))
        report_content.append(Paragraph(f"weight: {weight}", styles["BodyText"]))
        report_content.append(Spacer(1, 12))  # Add blank line
    report.build(report_content)