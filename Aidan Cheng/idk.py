Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:37:19) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
#lists/array

>>> myList = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
>>> myOtherList "a", "b", "c"
SyntaxError: invalid syntax
>>> myOtherList = "a", "b", "c"
>>> anotherList = "a", "b", "c", 1, 2, 3
>>> 
>>> print(myList[4])
5
>>> print(myOtherList[2])
c
>>> print(anotherList[1,2])

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(anotherList[1,2])
TypeError: tuple indices must be integers, not tuple
>>> shopingList = "chip", "soda", "burger king", "cats"
>>> shopingList.append("smashbros")

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    shopingList.append("smashbros")
AttributeError: 'tuple' object has no attribute 'append'
>>> shoppingList.append("smash")

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    shoppingList.append("smash")
NameError: name 'shoppingList' is not defined
>>> shopingList.append("smash")

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    shopingList.append("smash")
AttributeError: 'tuple' object has no attribute 'append'
>>> # shopingList.append("smash")
>>> # shopingList.append("smash")
>>> print(shopingList)
('chip', 'soda', 'burger king', 'cats')
>>> print(shopingList.append)

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(shopingList.append)
AttributeError: 'tuple' object has no attribute 'append'
>>> addToList = input("what do you need to add to the shoping list?")
what do you need to add to the shoping list? eggs

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    addToList = input("what do you need to add to the shoping list?")
  File "<string>", line 1, in <module>
NameError: name 'eggs' is not defined
>>> print(shopingList)
('chip', 'soda', 'burger king', 'cats')
>>> 
