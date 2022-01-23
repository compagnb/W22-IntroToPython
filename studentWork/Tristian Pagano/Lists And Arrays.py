#lists/array

mylist = 1, 2, 3, 4, 5, 6, 7, 8, 9,
myotherlist = "i", "h", "g"
anotherlist = "a", "b", "c", 1, 2, 3

print (mylist)

#index starts at 0

print (mylist[4]) #4 is the index for number 5
print (anotherlist[1])

shoppinglist = ["Doritos", "Dr Pepper", "Splatoon"]
shoppinglist.append("Zelda")
shoppinglist.remove("Doritos")

print(shoppinglist)

#Conditionals

#if(condition):
    #do this
    #else:
        #do that

userInput = input("guess my name")
if (userInput == "Tristian"):
    print("Correct")
else:
    print("Sorry")


