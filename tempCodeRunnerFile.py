from email.message import EmailMessage
import mimetypes
import os
import smtplib
import getpass

message = EmailMessage()
sender = "mbk73689@gmail.com"
recipient = "mbk7368@gmail.com"
body = """This is my first email to be sent from python directly"""
attachment_path = "C:\\Users\\mbk73\\Desktop\\Curriculum.txt"
filename = os.path.basename(attachment_path)

mimetype, _ = mimetypes.guess_type(attachment_path)
mime_type, mimesubtype = mimetype.split('/', 1)

message['from'] = sender
message['to'] = recipient
message['subject'] = f"greeting from {sender} to {recipient}"
message.set_content(body)

with open(attachment_path, "rb") as t:
    message.add_attachment(t.read(),maintype=mime_type,subtype=mimesubtype,filename=os.path.basename(attachment_path))

mailserver = smtplib.SMTP_SSL("smtp.gmail.com")
mailpass = getpass.getpass("736891177")
mailserver.login(sender, mailpass)
mailserver.send_message(message)
mailserver.quit()