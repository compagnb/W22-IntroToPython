import turtle

#def functionName (parameters):
#    pass

def drawShape(t,filled, size, fillColor, angle, sides, shape, xpos, ypos):
    t.speed(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
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
    

mike = turtle.Turtle()
drawShape (mike, "false", 200, "green", 170, 36, "square", 100, 100)

#mike = turtle.Turtle()
#mike.color("blue")
#mike.penup()
#mike.goto(100,100)
#mike.pendown()
#mike.begin_fill()
#mike.shape("turtle")
#for i in range (0,4): 
    #mike.forward(100)
    #mike.left(90)

#mike.end_fill()
