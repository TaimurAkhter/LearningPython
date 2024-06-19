# Date: 14th February 2024 Wednesday
# Start Time : 01 : 48 PM
# End Time : 02 : 18 PM


# from turtle import Turtle, Screen
# s1 = Screen()
# tom = Turtle()
# tom.speed("fastest")
# tom.color("red", "yellow")
# tom.pensize(1)

# tom.begin_fill()
# while True:
#     tom.forward(200)
#     tom.left(170)
#     if tom.heading() == 0:
#         break
# tom.end_fill()

# s1.exitonclick()

#-------------------------
import turtle
from turtle import Turtle, Screen
import random

s1 = Screen()
tom = Turtle()
tom.speed("fastest")
tom.pensize(1)
turtle.colormode(255)

while True:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tom.pencolor((r,g,b))
    tom.circle(100)
    tom.left(5)
    if tom.heading() == 0:
        break

s1.exitonclick()
