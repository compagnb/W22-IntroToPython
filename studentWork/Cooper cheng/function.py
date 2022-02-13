import turtle
##mike = turtle.Turtle()
##mike.shape("turtle")
##mike.color ("red")
##mike.begin_fill()
##mike.penup()
##mike.goto(100,100)
##mike.pendown()
##for i in range (0,4):
##    mike.forward(100)
##    mike.left(90)

##mike.end_fill()
def drawshape (t,filled,size,fillcolor,angle,sides,shape):
    t.color(fillcolor)
    t.shape(shape)
    for i in range (0, sides):
        t.forward(size)
        t.left(angle)
drawshape(mike, "false", 200,green, 90, 4"square")
          mike = turtle.turtle()          
