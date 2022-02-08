import random

numb = random.randint(1,10)
correctAnswer = False

userInput = input("pick a number between 1 and 10")
while correctAnswer == False:
    if(userInput == numb):
        print("YOU WIN")
        correctAnswer = True
    else:
        print("sorry you are worng the correct number was " + str(numb))
                     
        userInput = int(input("pick a number between 1 and 10"))

    
