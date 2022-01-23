# lists/ array

myList = 1,2,3,4,5,6,7,8,9,10
myOtherList = "a" , "b" ,"c"
anotherList = "a" , "b" , "c" ,1 ,2 ,3
print(myList[4])
print (anotherList[1])

shoppingList = ["icecream", "Dr.Pepper" , "Taco Bell"]
shoppingList.append("Minecraft")
print (shoppingList)
addToList = input ("what do you need to add to the shopping list")
print(addToList)
shoppingList.remove("Minecraft")
print (shoppingList)


#Conditionals

#if (condition) :
 #do this
 #else :
  # do that  


userInput = input("guess my name")
if(userInput == "Bryce"):
  print("correct")
elif (userInput == "Rauschenbach"):
  print("close")
else:
  print("sorry")
