import turtle

img = "invader.gif","invader1.gif", "invader2.gif", "invader3.gif",
"invader4.gif"

wn =  turtle.Screen()
for i in range(len(imgs)):
    wn.register_shape(img)[i])

for j in range(20):
    invaders.append(turtle.Turtle())
    if j % 2 == 0:
        invaders[j].shape(img[1])
    if j  % 3 == 0:
        invaders[j].shape(img[2])
    else:
        invaders[j].shape(img[0])

solosis = turtle.Turtle()
solosis.shape(img[1])
solosis.penup

def turnRight(t):
    t.right(30)
    
def turnLeft():
    t.left(30)

while True:
    solosis.forward(10)
    turnRight(solosis)

def speedUp():
    pass
def slowDown():
    pass

while True:
    solosis.forward(1)
