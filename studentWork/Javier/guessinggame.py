import random

numb = random.randint(0,4)
correctAnswer = False
playAgain = False
userInput = int(input("pick a number"))

while correctAnswer == False: 
 if(userInput == numb):
  print("You Win") 
  correctAnswer = True
 else:
  print("sorry you are wrong the correct number was " + str(numb))
  userInput = int(input("pick a number"))

