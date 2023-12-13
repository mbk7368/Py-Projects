#!/usr/bin/env python3

import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date

def read_text_files(folder_path):
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

def generate_report(filename, data):
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

        report_entry = f"name: {name}\nweight: {weight}"
        report_content.append(Paragraph(report_entry, styles["BodyText"]))
        report_content.append(Spacer(1, 12))  # Add blank line

    report.build(report_content)