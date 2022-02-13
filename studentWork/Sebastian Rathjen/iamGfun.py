import turtle

imgs = "invader1.gif", "invader1.gif"

wn = turtle.Screen()
wn.register_shape(ing)


gordo = turtle.Turtle()
gordo.shape(imgs)
Gordo.penup()

def TurnLeft(t):
    t.left(30)
    
def TurnRight(t):
    t.right(30)

while True:
    Gordo.forward(10)
    turnRight(Gordo)
    Gordo.forward(10)
    turnLeft(Gordo)


