import random

numb = random.radint(1,100)

userInput = input('pick a number')

if(userInput == numb):
    print('Hooray! You won! Have a cookie (:')
else:
    print('FOOL >:D! The correct number was " + str(numb))
