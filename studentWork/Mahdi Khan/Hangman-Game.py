#For a game of Hangman, what do we need?
#The word (and the letters that make it up!)
#The # of tries equals 6
#It is one try for each part of the hangman's body

word = ["Jacuzzi"]
amountOfTries = 6

import random
#.randint is a command that basically picks a random number between the numbers
#you have chosen. To separate the numbers, put a comma between the minimum and
#maximum values you desire.
number = random.randint(1,100) 
userInput = input("pick a number")

if(userInput == number):
    print("You win!")
else:
    print("Sorry bozo ur wrong the correct answer was " + str(number))
