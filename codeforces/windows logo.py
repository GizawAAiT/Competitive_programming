import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.pensize(3)
t.speed(1)
t.color("red")

# Move the pen to the starting position
t.penup()
t.goto(0, -200)
t.pendown()

# Draw the heart shape
t.begin_fill()

t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)

t.end_fill()

# Hide the turtle
t.penup()
t.hideturtle()

# Keep the window open until it is closed by user
turtle.mainloop()