import turtle


leonardo =  turtle.Turtle()
leonardo.shape("turtle")
leonardo.color("red")
sides = 0

#To start the beginning place of the turtle, use this command:
#The pen must be lifted so that when the turtle goes to the place on the grid,
#Then it doesn't draw behind it
#The numbers in leonardo.goto are the x and y values on the coordinate grid
leonardo.penup()
leonardo.goto(100,100)

#Use leonardo.pendown() to place the pen back down

leonardo.pendown()

#leonardo.forward(100)
#leonardo.right(90)
#leonardo.left(90)
#leonardo.backward(100)

#leonardo.forward(100)
#leonardo.left(90)
#leonardo.forward(100)
#leonardo.left(90)
#leonardo.forward(100)
#leonardo.left(90)
#leonardo.forward(100)

# while True: # this is an infinite loop it will never stop!
while sides < 4:
    leonardo.forward(100)
    leonardo.left(90)
    sides=sides+1

leonardo.penup()
leonardo.goto(-150,-150)

leonardo.pendown()
leonardo.color("orange")
leonardo.forward(75)
leonardo.penup()
leonardo.left(45)
leonardo.forward(75)
leonardo.pendown()
leonardo.forward(75)
leonardo.color("yellow")
leonardo.penup()
leonardo.left(45)
leonardo.forward(75)
leonardo.pendown()
leonardo.forward(75)
leonardo.color("green")
leonardo.penup()
leonardo.left(45)
leonardo.forward(75)
leonardo.pendown()
leonardo.forward(75)
leonardo.color("blue")
leonardo.penup()
leonardo.left(45)
leonardo.forward(75)
leonardo.pendown()
leonardo.forward(75)
leonardo.color("pink")
leonardo.penup()
leonardo.left(45)
leonardo.forward(75)
leonardo.pendown()
leonardo.forward(75)
leonardo.color("black")
leonardo.penup()
leonardo.left(45)
leonardo.forward(75)
leonardo.pendown()
leonardo.forward(75)
leonardo.left(45)
leonardo.color("red")
leonardo.penup()
leonardo.forward(75)
leonardo.pendown()
leonardo.forward(75)

#USE WHILE LOOPS TO SHORTEN THE AMOUNT OF CODE






