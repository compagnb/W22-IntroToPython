import random

numb = random. randit (1,100)

userInput = input("pick a number")

if(userInput == numb):
    print("You Win")
else:
    print("Sorry,you are wrong the correct number was" + str(numb))
