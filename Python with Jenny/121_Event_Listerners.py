# Date: 28th February 2024 Tuesday
# Now Time 10 : 00 AM
# Start Time: 10 : 08 AM
# End Time: 10 : 37 AM
from turtle import Turtle, Screen
screen = Screen()
tom = Turtle()

def up():
    tom.setheading(90) # tom.left(90)
    tom.forward(20)

def down():
    tom.setheading(270) # tom.right(90)
    tom.forward(20)

def left():
    tom.setheading(180)
    tom.forward(20)

def right():
    tom.setheading(0)
    tom.forward(20)

def clear_all():
    tom.clear()
    tom.penup()
    tom.home() # back to previous position
    tom.pendown()


# Turtle.listen()
screen.listen()
screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")
screen.onkey(fun=left, key="Left")
screen.onkey(fun=right, key="Right")
screen.onkey(fun=clear_all, key="c")

screen.exitonclick()