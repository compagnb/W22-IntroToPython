import turtle

bob = turtle.Turtle()
bob.shape("arrow")
bob.color("orange")
bob.begin_fill()
for i in range (0,4):
    bob.forward(100)
    bob.left(90)

bob.end_fill()

