import turtle

# Set up the turtle screen and set background color
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Set background picture (optional)
screen.bgpic("./Kitten.png")

# Create a turtle instance for the drawing pointer and set its properties
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("darkgreen")
my_turtle.pensize(3)

# Draw a square and fill the color
my_turtle.begin_fill()
for i in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)
my_turtle.end_fill()

# Exit the program when the user clicks the screen
screen.exitonclick()