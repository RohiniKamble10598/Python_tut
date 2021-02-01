text = input("Enter the teXT\n")


if("make a money a lot" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("Subscribe this" in text):
    spam = True
elif("click this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")
    