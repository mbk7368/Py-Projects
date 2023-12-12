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

def send_alert_email(subject):
    body = "Please check your system and resolve the issue as soon as possible."
    sender = "automation@example.com"
    recipient = "student@example.com"
    email_subject = f"Error - {subject}"
    message = emails.generate_email(sender, recipient, email_subject, body)
    emails.send_email(message)

def main():
    while True:
        cpu_usage_error = check_cpu_usage()
        disk_space_error = check_disk_space()
        memory_error = check_available_memory()
        name_resolution_error = check_name_resolution()

        if cpu_usage_error:
            send_alert_email("CPU usage is over 80%")
        if disk_space_error:
            send_alert_email("Available disk space is lower than 20%")
        if memory_error:
            send_alert_email("Available memory is less than 100MB")
        if name_resolution_error:
            send_alert_email("localhost cannot be resolved to 127.0.0.1")

        time.sleep(60)

if __name__ == "__main__":
    main()