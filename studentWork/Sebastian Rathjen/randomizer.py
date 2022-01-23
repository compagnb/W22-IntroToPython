import random

numb = random.randint(1,100)

userInput = input("Pick a number")

if(userInput == numb):
    print("You win")
else:
    print("Sorry you are wrong the correct number was " + str(numb))
