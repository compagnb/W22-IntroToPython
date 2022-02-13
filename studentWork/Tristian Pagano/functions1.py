import turtle

#def drawSquare(parameters):
#    pass

def drawShape(t, filled, size, fillColor, angle, sides, shape):
    t.speed(5)
    t.color(fillColor)
    t.shape(shape)
    for i in range(0, sides):
        t.forward(size)
        t.left(angle)
        
mike=turtle.Turtle()

drawShape(mike, "false", 69, "orange", 69, 69, "classic")


##turtle = turtle.Turtle()
##turtle.color("blue")
##turtle.penup()
##turtle.goto(100,100)
##turtle.pendown()
##turtle.begin_fill()
##for i in range(0,4):
##    turtle.forward(100)
##    turtle.left(90)
##
##turtle.end_fill()
