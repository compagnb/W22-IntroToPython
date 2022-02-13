import turtle

img = "invader1.gif"

wn = turtle.Screen()
wn.register_shape(img)

barb = turtle.Turtle()
barb.shape(img)
barb.penup()

def turnRight(t):
    t.right(30)

def turnLeft(t):
    t.left(30)

def speedUp():
    pass
def slowDown():
    pass

while True:
    barb.forward(10)
    turnRight(barb)
    barb.foward(10)
    turnLeft(barb)
