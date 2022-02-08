import turtle
mike = turtle.Turtle()
mike.color("orange")
raph = turtle.Turtle()
raph.color("purple")
don = turtle.Turtle()
don.color("blue")
leo = turtle.Turtle()
leo.shape("turtle")
sides = 0

##leo.forward(100)
##leo.left(90)
##leo.forward(100)
##leo.right(90)
##leo.backward(100)

leo.penup()
leo.goto(100,100)
leo.pendown()
leo.color("blue")

mike.penup()
mike.goto (-100,100)
leo.fill("blue")
leo.begin_fill()
# while True: # this is an infinate loop it will never stop!!
while sides < 4:
    leo.forward(100)
    leo.right(90)
    leo.left(60)
    leo.forward(100)
    leo.right(90)
    leo.left(60)
    leo.forward(100)
    leo.right(90)
    leo.left(60)
    sides=sides+1
leo.end_fill()

    



