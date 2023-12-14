import os
import csv
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")
def contents_of_file(filename):
  return_string = ""
  create_file(filename)
  with open(filename) as file:
    rows = csv.reader(file)
    next(rows)
    for row in rows:
      # Format the return string for data rows only
      return_string += "a {} {} is {}\n".format(row[1], row[0], row[2])
  return return_string
print(contents_of_file("flowers.csv"))
#--------------------------------------------------------------------------
import os
import csv
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")
def contents_of_file(filename):
  return_string = ""
  create_file(filename)
  with open(filename) as file:
    reader = csv.DictReader(file)
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string
print(contents_of_file("flowers.csv"))
#--------------------------------------------------------------------------
#!/usr/bin/env python3
import csv
def read_rmployees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

employee_list = read_rmployees('/home/USERNAME/data/employees.csv')
print(employee_list)

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data
#--------------------------------------------------------------------------
dictionary = process_data(employee_list)
print(dictionary)
#--------------------------------------------------------------------------
def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k]+'\n'))
        f.close()

write_report(dictionary, '/home/USERNAME/data/report.txt')

#--------------------------------------------------------------------------
import os
import sys
filename = sys.argv[1]
if not filename.endswith('.py'):
    filename += '.py'
if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("The is a new python file that were created\n")
else:
    os.remove(filename)
    with open(filename, 'w') as f:
        f.write("The is a new python file that were recreated\n")
    print(f"Attention, the file {filename} existed but were recreated again!")
sys.exit(0)
#--------------------------------------------------------------------------""
import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)",name)
    if result is None:
        return result
    return "{} {}".format(result[2], result[1])
rearrange_name("Lovelace, Ada")
rearrange_name("Musk, Elon")
#--------------------------------------------------------------------------
import shutil
import psutil
def disk_usage(disk):
    du = shutil.disk_usage(disk)
    freedisk = du.free / du.total * 100
    formatedper = "{:.2f}".format(freedisk)
    return float(formatedper) < 20
def process_check():
    usage = psutil.cpu_percent(10)
    return usage > 75
if disk_usage("/"):
    print("The free disk space available is too low, a check is needed.\n")
if process_check():
    print("The processor is over-utilized, a check is needed.\n")
if not process_check() and not disk_usage("/"):
    print("Everything is OK, no action is needed.")
#--------------------------------------------------------------------------
import shutil

def disk_usage(disk):
    du = shutil.disk_usage(disk)
    freedisk = du.free / du.total * 100
    formatedper = "{:.2f}".format(freedisk)
    return float(formatedper) < 30

if disk_usage("C:\\"):
    print("\n The free disk space available is too low, a check is needed.\n")
if not disk_usage("c:\\"):
    print("\n Everything is Ok, no action needed \n ")
#--------------------------------------------------------------------------
guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()
with open("guests.txt") as guests:
    for line in guests:
        print(line.split())
#--------------------------------------------------------------------------
import os
print(f"The app data variable: {os.environ.get('APPDATA','the variable does not exist')}" )
print(f"The path variable: {os.environ.get('PATH','The variable does not exis')}")
#--------------------------------------------------------------------------
import os
import sys
filename = sys.argv[1]
if not filename.endswith('.py'):
    filename += '.py'
if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("The is a new python file that were created\n")
else:
    os.remove(filename)
    with open(filename, 'w') as f:
        f.write("The is a new python file that were recreated\n")
    print(f"Attention, the file {filename} existed but were recreated again!")
sys.exit(0)
#--------------------------------------------------------------------------
import os
import sys
import subprocess
filename = sys.argv[1]
if not filename.endswith('.py'):
    filename += '.py'
if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f
#       f.write("""count=10\nfor i in range(count):\n\tprint(f'i am Line {i} in the python code that were created from another code and excuted successfully')\n""")
#else:
#    os.remove(filename)
#    with open(filename, 'w') as f:
#        f.write("""print("This is a new python file that were recreated")\ncount=10\nfor i in range(count):\n\tprint(f"i am Line {i} in the python code that were created from another code and excuted successfully")\n""")
#    print(f"Attention, the file {filename} existed but were recreated again!")
#subprocess.call(['python',filename])
#sys.exit(0),
#--------------------------------------------------------------------------
import sys
filename = sys.argv[1]
def count_character(filename):
    try:
        f = open(filename)
    except OSError:
        return None
    characters = {}
    for line in f:
        for char in line:
            if char != ' ':
                characters[char] = characters.get(char, 0) +1
    f.close()
    return characters
character = count_character(filename)
def biggest_char(character):
    max_char = ""
    max_count = 0
    for char, count in character.items():
        if count > max_count:
            max_count = count
            max_char = char
    character_count = {max_char: max_count}
    return character_count
character_count = biggest_char(character)
print(character_count)

#--------------------------------------------------------------------------

#--------------------------------------------------------------------------

#--------------------------------------------------------------------------

#--------------------------------------------------------------------------

#--------------------------------------------------------------------------

#--------------------------------------------------------------------------

#--------------------------------------------------------------------------

#--------------------------------------------------------------------------

#--------------------------------------------------------------------------

#--------------------------------------------------------------------------