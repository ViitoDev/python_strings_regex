import re

cpf = input("Enter the cpf on format XXX.XXX.XXX-XX:\n")
cpf_pattern = r'\d{3}.\d{3}.\d{3}-\d{2}'
result = re.search(cpf_pattern, cpf)

if result:
    print("Valid cpf")
else: 
    print("Invalid cpf")