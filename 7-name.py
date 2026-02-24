import re

name = str(input("Enter the name:\n"))
name_pattern = r'[a-zA-Z]'
result = re.search(name_pattern,name)

if result:
    print("Valid name!")
else:
    print("Invalid name!")