#A List is another type of variable!
#It is also known as an array
#Lists can contain only numbers
#Lists can contain only string
#Lists can contain both numbers and string
myList = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
myOtherList = "a", "b", "c"
anotherList = "a", "b", "c", 1, 2, 3,
#Computers are STUPID! WE HAVE TO TELL THEM WHAT TO DO AND ALWAYS REMEMBER THIS!
#Computers also count the first "term" or "thing" within a list as the 0th TERM!
#SO IN myList, the number 1 in myList is known as the 0th term!
#If we were to input the 4th term into myList, then we would get the number 5!
print(myList[4])
print(anotherList[1])
#When making lists, brackets are required
#Putting .append and adding something to the list will add it, and
#putting .remove and writing something you want to remove will remove it!
shoppingList = ["Doritos", "Coke", "Splatoon"]
shoppingList.append("Zelda")
shoppingList.append("Milk")
shoppingList.remove("Doritos")
print(shoppingList)

#Conditionals
#Conditionals are made with if statements

#if(condition) :
# do this
# else
#  do that

#These four comments preceding this comment mean that if there is something that
#satisfies the condition then it goes in front of that colon, but if it doesn't then
#the else will tell it to do something else
#WHEN WRITING IF STATEMENTS AND YOU ARE WRITING THE ANSWER, THEN A DOUBLE
#EQUALS SIGN IS REQUIRED 
#Also if you want to add multiple conditions or "answers" for the if(UserinPut
#to equal to, then hit enter and write "elif" and write a new string or number
#for userInput to equal to! Also don't forget to write print() and write what happens
#when you write your answer
userInput = input("guess my name")
if(userInput == "Barb"):
    print("correct")
elif(userInput == "Mahdi"):
    print("correct")
else:
    print("no ur wrong u clown get better L dance")

