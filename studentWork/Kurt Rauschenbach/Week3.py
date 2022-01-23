#lists/array

myList = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
myOtherList = "g", "h", "i"
anotherList = "a", "b", "c", 1, 2, 3

print(myList[4])
print (anotherList[1])

shoppingList = ["Dr.Pepper", "Doritos", "Wendys"]
shoppingList.append("Fortnite")

addToList = input(" what do you need to add to the shoping list.")
shoppingList.append(addToList)
print(addToList)
print(shoppingList)
shoppingList.remove("Wendys")


#Conditionals

#if(condition):
# do this
# eles:
#   do that

userInput = input("guess my name")
if(userInput == "Kurt"):
  print("CORRECT")
elif(userInput == "Bryce"):
    print("Close")
else:
    print("sorry")
