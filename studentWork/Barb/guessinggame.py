import random

numb = random.randint(1,100)

userInput = input("pick a number")

if(userInput == numb):
  print("You Win")
else:
  print("sorry you are wrong the correct number was " + str(numb))
