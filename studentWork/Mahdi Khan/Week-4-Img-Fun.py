import turtle
#WN means window
img = "Invader1.gif", "invader2.gif"

wn = turtle.Screen()
wn.register_shape(img)


barbJR = turtle.Turtle()
barbJR.shape(img)
barbJR.penup()


def turnRight(t):
    t.right(30)

def turnLeft(t):
    t.left(30)
    
def speedUp():
    t.speed()
    
def slowDown():
    t.speed()


#AN INFINITE WHILE LOOP IS JUST USING "while True:"
while True:
    barbJR.forward(10)
    turnRight(barbJR)
    
    
    
