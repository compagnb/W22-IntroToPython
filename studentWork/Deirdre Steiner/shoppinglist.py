Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:37:19) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
myList = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
myOtherList = "g", "h", "i"
anotherFuckingList = "a", "b", "c", 1, 2, 3

print(mylist[4])
print(anotherFuckingList[1])

shoppingList = ["Doritos", "Dr.Pepper", "Splatoon"]
shoppingList.append('Zelda')

addTOList = input("what needs to be added?")
shoppingList.append(addToList)
shoppingList.remove("Doritos")

print(shoppingList)
