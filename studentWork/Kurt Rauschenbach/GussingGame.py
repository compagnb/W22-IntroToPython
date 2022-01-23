import random

numb = random.randint(1,10)

userInput = input("pick a number")

if(userInput == numb):
    print("YOU WIN")
else:
    print("sorry you are worng the correct number was " + str(numb))
