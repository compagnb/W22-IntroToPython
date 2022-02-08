import turtle
screen= turtle.Screen()
mike = turtle.Turtle()
mike.color("orange")
mike.shape("square")
raph = turtle.Turtle()
raph.color("red")
don = turtle.Turtle()
don.color("purple")
leo = turtle.Turtle()
leo.color("blue")
leo.shape("turtle")
sides = 0
screen.bgcolor("black")

raph.penup()
raph.goto(-100,-100)
raph.pendown()
raph.width(3)
raph.fillcolor("black")
raph.begin_fill()
raph.circle(20)
raph.end_fill()

mike.penup()
mike.goto(-100,100)
mike.pendown()

leo.penup()
leo.goto(100, 100)
leo.pendown()

# while True: # this is an infinate loop it will never stop!!
leo.begin_fill()
mike.width(5)
mike.fillcolor("red")
mike.begin_fill()
while sides < 4:
    leo.forward(100)
    mike.forward(100)
    leo.right(90)
    mike.right(90)
    sides=sides+1
leo.end_fill()
mike.end_fill()

    
