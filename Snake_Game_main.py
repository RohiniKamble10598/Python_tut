# Snake water gun Game OR Rock paper Scissors
import random

def gameWin(comp, you):
    # When two values are same! declair tie
    if comp==you:
        return None
        # check computer possibilities choose comp=s
    elif comp =='s':
        if you=='w':
            return False
        elif you=='g':
            return True
        
        # check computer possibilities choose comp=w
    elif comp =='w':
        if you=='g':
            return False
        elif you =='s':
            return True
        
        # check computer possibilities choose comp=g
    elif comp =='g':
        if you =='s':
            return False
        elif you =='w':
            return True
        

print("comp Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, you)
print(f"comp choose {comp}")
print(f"you choose {you}")
if a == None:
    print("The game is tie!")
elif a:
    print("you Won!")
else:
    print("You Lose!")