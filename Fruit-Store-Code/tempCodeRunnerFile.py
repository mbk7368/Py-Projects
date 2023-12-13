#!/usr/bin/env python3

import os
from datetime import date
import emails

def send_email(sender, recipient, subject, body, attachment_path):
    message = emails.generate_email(sender, recipient, subject, body, attachment_path)
    emails.send_email(message)
