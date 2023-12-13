#!/usr/bin/env python3

from datetime import date
import smtplib
from email.message import EmailMessage
import mimetypes
import getpass

def generate_email(sender, receiver, subject, body, attachment):
    message = EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)
    attachment_file_name = "processed.pdf"

    mime_type, _ = mimetypes.guess_type(attachment)
    mime_type, mime_subtype = mime_type.split("/", 1)

    with open(attachment, "rb") as attachment_file:
        message.add_attachment(
            attachment_file.read(),
            maintype=mime_type,
            subtype=mime_subtype,
            filename=attachment_file_name, )
    return message

def send_email(message):
    server =  smtplib.SMTP('localhost')
    try:
        server.send_message(message)
        print("Email sent successfully!")
        server.quit()
    except Exception as e:
        server.quit()
        print("An error occurred while sending the email:", str(e))

# Example usage:
sender_email =      "automation@example.com"
receiver_email =    "student@example.com"
subject =           "Upload Completed - Online Fruit Store"
body =              "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
attachments =       "/tmp/processed.pdf"
message = generate_email(sender_email,receiver_email,subject,body,attachments)
send_email(message)