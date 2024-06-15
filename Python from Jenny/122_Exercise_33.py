# Date: 28th February 2024 Tuesday
# Start Time: 10 : 38 AM
# End Time 10 : 48 AM

from turtle import Turtle, Screen
screen = Screen()
tom = Turtle()

def move_forward():
    tom.forward(10)

def move_backward():
    tom.backward(10)

def turn_left():
    new_heading = tom.heading()+10
    tom.setheading(new_heading)
    tom.forward(5)

def turn_right():
    new_heading = tom.heading()-10
    tom.setheading(new_heading)
    tom.forward(5)

def clear_all():
    tom.clear()
    tom.penup()
    tom.home() # back to previous position
    tom.pendown()


# Turtle.listen()
screen.listen()
screen.onkey(fun=move_forward, key="Up")
screen.onkey(fun=move_backward, key="Down")
screen.onkey(fun=turn_left, key="Left")
screen.onkey(fun=turn_right, key="Right")
screen.onkey(fun=clear_all, key="c")


screen.exitonclick()

# Now Time : 10 : 47 AM     # Zumar