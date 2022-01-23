#Anything following a hashtag and is red is a comment
#Variables!!!
#Cant Have In A Variable Name:
#NOspaces - However you can use CamelCase (Uppercase every new word and it will serve as a space) or under_scores
#capital letters - These are reserved for other functions


name = "Mahdi" #this is a string
age = 14 #This number is an integer (Whole Number)
pi = 3.14 #However decimals like pi are called floats (decimals)
favPie = "Apple"


#Strings
#Must be surrounded by quotes
#They both need to be either " or '
#If you have a conjunction then surround it in " or '
#The pair of quotes need one type of quote so either " or ' not a mx of both
#To add an Int(Integer) to a string we have to mask the int using str()
#This is because integers and strings can't be added in a sentence without masking them
hereFirst = "Bryce & Kurt"
said = "said We won't have any vocabulary today'"
space = " "
print(hereFirst + space + said)



#Objective: Create a sentence that says "Hi, my name is (name) and I am (#) years old
#To add an Int(Integer) to a string we have to mask the int using str()
#This is because integers and strings can't be added in a sentence without masking them
red = "Hi my name is "
orange = ", and my age is "
sentence = red + name + orange + str(age)
print(sentence)

flip = int(name) * int(age)
print(flip)
