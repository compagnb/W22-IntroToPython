import turtle

leo = turtle.Turtle()
leo.shape("turtle")
leo.color("lime green")
sides = 0


while sides < 8:
    leo.forward(100)
    leo.right(45)
    sides=sides+1
