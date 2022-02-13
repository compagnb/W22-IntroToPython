import turtle

#mahdiJR = turtle.Turtle()
#mahdiJR.shape("turtle")
#mahdiJR.color("purple")
#mahdiJR.begin_fill()
#FOR LOOPS ARE ITERATIVE!
#THE (0,4) MEANS THAT THE CODE WILL REPEAT FOUR TIMES!
#THE i CAN BE ANY LETTER OR WORD!
#IF YOU REPLACE I WITH "APPLE" IT WILL STILL WORK!
#DO mahdiJR.speed(5) TO CHANGE THE SPEED FROM 1-10 (1 being the slowest and 10 being the fastest)!
#mahdiJR.penup()
#mahdiJR.goto(100,100)
#mahdiJR.pendown()
#for i in range(0,4):
#    mahdiJR.forward(100)
#    mahdiJR.left(90)
#mahdiJR.end_fill()

#def functionName(parameters)
#    pass
#the t in the parenthesis is a placeholder and represents 
#def drawShape(t, filled, size, fillColor, angle, sides, shape):
#AND
#drawShape(mahdiJR, "false", 200, "purple", 90, 4, "square")
#FOR THE drawShape YOU NEED A DEFINITION FOR EACH PARAMETER (the different words in the parenthesis)! 
def drawShape(t, filled, size, fillColor, angle, sides, shape, xposition, yposition):
    t.speed(10)
    t.penup()
    t.goto(xposition, yposition)
    t.pendown()
    t.color(fillColor)
    if filled == True:
        t.begin_fill()
    t.shape(shape)
    for i in range(0,sides):
        t.forward(size)
        t.left(angle)
    if filled == True:
        t.end_fill()
    t.hideturtle()
    #t.hideturtle() HIDES THE TURTLE
mahdiJR = turtle.Turtle()
drawShape(mahdiJR, True, 200, "purple", 170, 36, "triangle", 100, 100)
#You can change the True to False so that the shape doesn't get filled in at the end!
