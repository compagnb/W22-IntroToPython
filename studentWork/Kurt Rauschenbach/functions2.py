import turtle

#def functionName(parameters):
#   pass

def drawShape(t, filled, size, fillColor, angle, sides, shape):
    t.color(fillColor)
    t.shape(shape)
    for i in range(0, sides):
        t.forward(size)
        t.left(angle)

        
mike = turtle.Turtle()

drawShape(mike, "false", 200, "red", 90, 4, "square")
                     

#mike.shape("turtle")
#mike.color("blue")
#mike.penup()
#mikegoto(100,100)
#mike.pendown()
#mike.begin_fill()
#for i in range(0,4):
    #mike.forward(100)
    #mike.left(90)
    #mike.end_fill
 
