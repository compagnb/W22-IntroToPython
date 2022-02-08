import turtle

leo = turtle.Turtle()
leo.shape("square")
sides = 0

#leo.forward(100)
#leo.left(90)
#leo.forward(100)
#leo.left(90)
#leo.backward(100)
leo.color("black")



# while True: # this is an infinite loop it will never stop!!
#while sides < 4:
 #   leo.forward(100)
  #  leo.right(90)
   # side=sides+1

#leo.forward(125)
#leo.right(45)
#leo.color("white")
#leo.forward(125)
#leo.right(45)
#leo.color("black")
#leo.forward(125)
#leo.right(45)
#leo.color("white")
#leo.forward(125)
#leo.right(45)
#leo.color("black")
#leo.forward(125)
#leo.right(45)
#leo.color("white")
#leo.forward(125)
#leo.right(45)
#leo.color("black")
#leo.forward(125)
#leo.right(45)
#leo.color("white")
#leo.forward(125)
#leo.right(45)


leo.penup()
leo.goto(0,-150)
leo.pendown()
leo.begin_fill()
leo.color("magenta")
leo.fillcolor("black")
leo.width(20)
leo.circle(200)
leo.end_fill()

toby = turtle.Turtle()
toby.shape("square")
toby.color("magenta")
toby.penup()
toby.pendown()
toby.goto(-300,100)
toby.left(25)
toby.forward(30)

