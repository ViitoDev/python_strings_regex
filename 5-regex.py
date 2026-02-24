import re

recipe = input("Enter your receipt:\n")
recipe_number = re.findall(r'\d+', recipe)[0]
print(f"The number of recipe is: {recipe_number}")