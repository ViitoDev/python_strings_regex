import re

phrase = str(input("Type the text to be revised:\n"))
word = str(input("Which word do you want to replace?\n"))
new_word = str(input("What's the new word?\n"))
new_phrase = re.sub(rf'\b{word}\b', new_word, phrase)
print(new_phrase)