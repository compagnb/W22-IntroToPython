import turtle

#def functionName(parameter):
#    pass

def drawShape(t, filled, size, fillcolor, angle, sides, shape, xpos, ypos):
    t.speed(100)
    t.penup()
    t.goto(xpos, ypos)
    t.pendown()
    t.color(fillcolor)
    if filled == True:
        t.begin_fill()
    t.shape(shape)
    for i in range(0, sides):
        t.forward(size)
        t.left(angle)
    if filled == True:
        t.end_fill()
    t.hideturtle()

mike = turtle.Turtle()
#drawShape(mike, True, 210, "gold", 170, 36, "square", 100, 100)
##
##for b in range(0, 40):
##    drawShape(mike, False, 100+b, "blue", 100+b, 36, "turtle", b-10, b+10)
##

