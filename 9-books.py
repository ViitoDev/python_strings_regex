import re

book =  input("Enter the book name:\n")
Initial_letter = input("Enter the initial letter:\n")
words = re.findall(rf'\b{Initial_letter}[a-zá-ÿ]*', book, re.IGNORECASE)
print(words)