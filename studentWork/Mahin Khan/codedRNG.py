import random

numb = random.randint(1,100)
correctAnswer = False
playAgain = False 
userInput = int(input("pick a number"))

while correctAnswer == False:
  if(userInput == numb):
    print("Hooray! You won! Have a cookie :D")
    correctAnswer = True
  else:
    print("FOOL >:D! The correct number was " + str(numb))
    userInput = int(input("pick a number"))
