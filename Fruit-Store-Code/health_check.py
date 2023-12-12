#!/usr/bin/env python3

import time
import psutil
import socket
import emails

def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > 80:
        return "CPU usage is over 80%"
    return ""

def check_disk_space():
    disk_usage = psutil.disk_usage("/")
    if disk_usage.percent > 80:
        return "Available disk space is lower than 20%"
    return ""

def check_available_memory():
    memory = psutil.virtual_memory()
    if memory.available < 100 * 1024 * 1024:  # 100MB
        return "Available memory is less than 100MB"
    return ""

def check_name_resolution():
    try:
        ip_address = socket.gethostbyname("localhost")
        if ip_address != "127.0.0.1":
            return "Hostname 'localhost' cannot be resolved to '127.0.0.1'"
    except socket.error:
        return "Hostname 'localhost' cannot be resolved"
    return ""

def send_alert_email(subject, body):
    sender = "automation@example.com"
    recipient = "student@example.com"
    email_subject = subject
    email_body = body
    message = emails.generate_email(sender, recipient, email_subject, email_body)
    emails.send_email(message)

def main():
    while True:
        cpu_usage_error = check_cpu_usage()
        disk_space_error = check_disk_space()
        memory_error = check_available_memory()
        name_resolution_error = check_name_resolution()

        if cpu_usage_error or disk_space_error or memory_error or name_resolution_error:
            error_subject = "Error - System Alert"
            error_body = "Please check your system and resolve the issue as soon as possible.\n\n"

            if cpu_usage_error:
                error_body += "Error - " + cpu_usage_error + "\n\n"
            if disk_space_error:
                error_body += "Error - " + disk_space_error + "\n\n"
            if memory_error:
                error_body += "Error - " + memory_error + "\n\n"
            if name_resolution_error:
                error_body += "Error - " + name_resolution_error + "\n\n"

            send_alert_email(error_subject, error_body)

        time.sleep(60)

if __name__ == "__main__":
    main()