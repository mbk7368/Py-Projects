#!/usr/bin/env python3

import os
from datetime import date
import reports
from reports import read_text_files
from reports import generate_report
from email.message import EmailMessage
import mimetypes
import smtplib
import getpass

folder_path = "/home/student/supplier-data/descriptions"
data = read_text_files(folder_path)
report1 = generate_report("/tmp/processed.pdf", data)


def main():
    # Generate the report text
    report_text = ""
    for item in data:
        report_text += f"name: {item['name']}\nweight: {item['weight']}\n\n"

    sender = "automation@example.com"
    recipient = "student@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = "/tmp/processed.pdf"

    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    with open(attachment_path, "rb") as file:
        attachment_data = file.read()
        mimetype, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mimetype.split('/', 1)
        message.add_attachment(attachment_data, maintype=mime_type, subtype=mime_subtype,
                               filename=os.path.basename(attachment_path))

    mailserver = smtplib.SMTP("localhist")
    mailpass = getpass.getpass("Enter your email password: ")
    mailserver.login(sender, mailpass)
    mailserver.send_message(message)
    mailserver.quit()


if __name__ == "__main__":
    main()