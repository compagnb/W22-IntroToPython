#hangman
#what do we need?
# word (and the letters that make it up)
# amount of tries (6)

import random

numb = random.randint (1,100)
correctAnswer = False
userInput = input("pick a number")

while correctAnswer == False:
 if(userInput == numb):
    print("You win")
    correctAnswer = True 
 else:
    print("sorry you are wrong, the correct number was " + str(numb))
    userInput = int(input("pick a number"))
    correctAnswer = False

