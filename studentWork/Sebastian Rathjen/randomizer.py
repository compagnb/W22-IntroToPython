import random

numb = random.randint(1,100)
correctAnswer = False
userInput = input("Pick a number")

while correctAnswer == False:
 if(userInput == numb):
    print("You win")
    correctAnswer = True
 else:
    print("Sorry you are wrong the correct number was " + str(numb))
    userInput = input("Pick a number")
    
    import random
    numb = random.randint(1,100)

