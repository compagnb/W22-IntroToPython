import turtle
mike = turtle.Turtle()
mike.color("black")
mike.speed(10)
sides = 0

mike.penup()
mike.goto(-10,10)
mike.pendown()

# while True: # this is an infinate loop it will never stop!!
mike.width(5)
mike.fillcolor("gray")
mike.begin_fill()
while sides < 10:
    mike.forward(632)
    mike.left(123)
    mike.right(321)
    mike.forward(123)
    sides=sides+1
mike.end_fill()
