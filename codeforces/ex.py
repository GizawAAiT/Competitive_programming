import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()

# Draw a Black Circular Avatar Background
t.penup()
t.goto(0, -100)  # Position the turtle
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(100)  # Draw a circle with radius 100
t.end_fill()

# Write "NETFLIX" with red text color
t.penup()
t.goto(-40, -10)  # Position the turtle
t.pencolor("red")
t.pendown()
t.write("NETFLIX", font=("Arial", 36, "bold"))

# Keep the window open
turtle.done()