letter = '''Dear <|Name|>,
Greeting From ABC Coding House .i am to tell you About your selection
YOu are selceted!
Date: <|Date|> '''
name = input("Enter your name\n")
date = input("Enter Date\n")
letter = letter.replace("<|Name|>" , name)
letter = letter.replace("<|Date|>" , date)
print(letter)