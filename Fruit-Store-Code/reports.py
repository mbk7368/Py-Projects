#!/usr/bin/env python3

import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date

folder_path = "supplier-data/descriptions"

def read_text_files(folder_path):
    data = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as file:
                content = file.read().strip()

                data.append({"description": content})
    return data

def generate_report(filename, data):
    today = date.today().strftime("%B %d, %Y")
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_content = []
    report_title = Paragraph(f"Processed Update on {today}", styles["h1"])
    report_content.append(report_title)
    report_content.append(Spacer(1, 12))  # Add blank line

    for item in data:
        description = item["description"]

        report_content.append(Paragraph(description, styles["BodyText"]))
        report_content.append(Spacer(1, 12))  # Add blank line

    report.build(report_content)

data = read_text_files(folder_path)
generate_report("processed.pdf", data)