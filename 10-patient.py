import re

patient = input("Enter the patient's full name and year of birth (format: name second - year):\n")
pattern = r'(\w+) (\w+) - (\d{4})'
result = re.search(pattern, patient)

if result:
    first_name = result.group(1)
    second_name = result.group(2)
    born_year = result.group(3)
    print(f"First name: {first_name}")
    print(f"Second name: {second_name}")
    print(f"Born year: {born_year}")
else:
    print("Invalid format.")