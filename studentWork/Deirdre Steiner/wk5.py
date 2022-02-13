import turtle

def drawShape (t, filled, size, fillColor, angle, sides, shape):
    t.speed(10)
    t.penup()
    t.goto(xpos,ypos)
    t.pendown()
    t.color(fillColor)
    if filled == True:
        t.begin_fill()
    t.shape(shape)
    for i in range (0, sides):
        t.forward(size)
        t.left(angle)
    if filled == True:
        t.end_fill()


bob = turtle.Turtle()

for b in range(0, 20):
    drawShape(bob, False, 100*b, "pink", 100*b, 36, "turtle", b*10, b*10)
    drawShape(bob, True, 200, "pink", 170, 36, "turtle", 100, 100)
