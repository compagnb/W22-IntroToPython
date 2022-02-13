import turtle

#def functionName(parameters):
#    pass




def drawShape(t, filled, size, fillColor, angle, sides, shape, xpo, ypo):
    t.penup()
    t.goto(xpo, ypo)
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


kai = turtle.Turtle()    
#drawShape (kai, False, 200, "green", 90, 4, "triangle", 100, 100)

for b in range(0, 20):
    if b % 2 == 0:
        drawShape(kai, False, b*100, "blue", 100, 36, "turtle", b*10, b*10)
    else:
        drawShape(kai, False, b*100, "red", 100, 36, "turtle", b*10, b*10)

    
##kai = turtle.Turtle()
##kai.shape("square")
##kai.color("magenta")
##kai.penup()
##kai.goto(0,-150)
##kai.pendown()
##kai.speed(500)
##kai.begin_fill()
##for i in range(0,4):
##    kai.forward(100)
##    kai.right(90)
##kai.end_fill()


