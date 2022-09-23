letter = '''Dear <|NAME|>
   you are selected
   in <|DATE|>
'''

name = input("Enter your name\n")
date = input("Enter Date\n")
# date = int(date)
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
