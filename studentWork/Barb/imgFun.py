import turtle
import random


imgs ="invader.gif", "invader1.gif", "invader2.gif", "invader3.gif", "invader4.gif"
invaders = []
wn = turtle.Screen()
wn.tracer(3)

for i in range(len(imgs)):
    wn.register_shape(imgs[i])

for j in range(20):
    invaders.append(turtle.Turtle())
    if j % 2 == 0:
        invaders[j].shape(imgs[1])
    if j % 3 == 0:
        invaders[j].shape(imgs[2])
    else:
        invaders[j].shape(imgs[0])

barb = turtle.Turtle()
barb.shape(imgs[1])
barb.penup()

def turnRight(t):
    t.right(30)
    
def turnLeft(t):
    t.left(30)

while True:
    barb.forward(10)
    turnRight(barb)
    for invader in invaders:
        invader.penup()
        invader.forward(random.randint(0,10))
        turnLeft(invader)
