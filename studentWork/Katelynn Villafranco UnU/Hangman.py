#handman
#what do we need?
# word (and the letters that make it up)
#amount of tries (6)

words = ["dumpling"]
amtTries = 6

import random

numb = random,randit(1,100)

userInput = input("pick a number")

if(userInput == numb):
    print("You Win! You are a princess UwU")
else:
    print("sorry you are incorrect the correct answer was " + str(numb))
