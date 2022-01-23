#list/array

myList = 1, 2, 3, 4, 5,  6, 7, 8, 9, 10
myOtherList = "a", "b", "c"
anotherList = "a", "b", "c", 1, 2, 3
print(myList[4])
print(anotherList[1])



shopingList = ["Milk", "razen bread", "sugar", "donuts"]
shopingList.append("Zelda")
print(shopingList)

addToList = input("what needs to be added.") 
shopingList.append(addToList)
shopingList.remove("sugar")

print("shopingList")







#if(condition):
#    do this
#    else:
#        do that


userInput = input("guess my name")
if(userInput == "Seb"):
    print("correct my name is Seb")
elif(userInput == "Bella"):
    print("Your a dum dum")
else:
    print("sorry your wrong, Maybe try again next time")


