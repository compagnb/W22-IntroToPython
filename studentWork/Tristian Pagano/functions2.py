import turtle

#def functionName(parameters):
#    pass

def drawShape(t, filled, size, fillColor, angle, sides, shape, xpos, ypos):
    t.speed(5)
    t.penup()
    t.goto(xpos, ypos)
    t.pendown()
    t.color(fillColor)
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
drawShape(mike, False, 200, "orange", 170, 36, "classic", 100, 100)








##mike.shape("turtle")
##mike.color("blue")
##mike.penup()
##mike.goto(100,100)
##mike.pendown()
##mike.begin_fill()
##for i in range(0,4):
##    mike.forward(100)
##    mike.left(90)
##
##mike.end_fill()
