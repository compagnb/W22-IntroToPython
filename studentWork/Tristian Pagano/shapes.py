import turtle

leo = turtle.Turtle()
leo.shape("turtle")
sides = 0

#leo.forward(100)
#leo.left(90)
#leo.forward(100)
#leo.right(90)
#leo.backward(100)

leo.penup()
leo.goto(100, 100)
leo.pendown()
leo.color("blue")

# while True: # this is an infinate loop it will never stop!!
while sides < 4:
    leo.forward(100)
    leo.right(90)
    sides=sides+1

    
    
