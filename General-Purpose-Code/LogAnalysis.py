##!/usr/bin/env python3

import re
import csv

logfile =  input("Enter the path to the log file:")
userstatpath = input("Enter the path where you want the statistics file to be saved:")
errorlogpath = input("Enter the path where you want the ErrorLogs file to be saved:")

def main():
  userstats_to_csv(userstatpath)
  errorlogs_to_csv(errorlogpath)
  if __name__ == "__main__":
    main()

def error_logs():
    with open(logfile, 'r') as file:
        syslogdata = file.readlines()
        error_count = {}
        for line in syslogdata:
            errors = re.search(r"ERROR [\w \']+", line)
            if errors:
                error_string = str(errors.group())
                error_content = re.sub(r"ERROR ","",error_string)
                if error_content in error_count:
                    error_count[error_content] += 1
                else:
                    error_count[error_content] = 1
        sorted_error_count = sorted(error_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_error_count         
def errorlogs_to_csv(file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Error', 'Count'])
        data = error_logs()
        writer.writerows(data)
def user_stats():
    with open(logfile, 'r') as file:                        
        syslogdata = file.readlines()
        users = {}
        output = []
        pattern = r"[\w :.]+(INFO|ERROR)([\w :.#\[\]])+?\(([\w]+)\)"
        for line in syslogdata:
            string = re.search(pattern,line)
            if string:
                user = str(string.group(3))
                error_type = str(string.group(1))
                if user in users:
                    if error_type in users[user]:
                        users[user][error_type] += 1
                    else:
                        users[user][error_type] = 1
                else:
                    users[user] = {error_type: 1}
        sorted_users = sorted(users.items())
    for user, error_type in sorted_users:
        sorted_errortype = sorted(error_type.items())
        error_count = 0
        info_count = 0    
        for ertype, count in sorted_errortype:
            if ertype == "ERROR":
                error_count = count
            elif ertype == "INFO":
                info_count = count       
        output.append(f"{user} {error_count} {info_count}")
    return output
def userstats_to_csv(file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'INFO', 'ERROR'])
        data = user_stats()
        for row in data:
            writer.writerow(row.split())