# Date: 15th February 2024 Thursday
# Start Time : 01 : 39 PM
# End Time : 02 : 01 PM

import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

tom = Turtle()
tom.speed("fastest")

s1 = Screen()
s1.screensize(500,500)
print(s1.screensize())

for i in range(5):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tom.pencolor((r,g,b))
    tom.dot(20)
    tom.penup()
    tom.goto(random.randint(0, 200), random.randint(0, 200))
    tom.pendown()

s1.exitonclick()