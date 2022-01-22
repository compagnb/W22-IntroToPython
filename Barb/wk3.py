#lists/array

myList = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
myOtherList = "g", "h", "i"
anotherList = "a", "b", "c", 1, 2, 3

print(myList[4])
print(anotherList[1])

shoppingList = ["Doritos", "Dr. Pepper", "Splatoon"]
shoppingList.append('Zelda')

addToList = input("what needs to be added.")
shoppingList.append(addToList)
shoppingList.remove("Doritos")

print(shoppingList)

#Conditionals

#if(condition):
# do this
# else:
#   do that

userInput = input("guess my name")
if(userInput == "Barb"):
  print("Correct")
elif(userInput == "Mahdi"):
  print("Close")
else:
  print("sorry")
  















