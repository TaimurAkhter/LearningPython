# ----------Date: 13th February 2024 Tuesday
# ------Start Time : 02 : 04 PM
# ------End Time : 02 : 20 PM

# Random Walk

import turtle
from turtle import Turtle, Screen
import random
# random.randrange(0, 360, 90) # 0 90 180 270
direction = [0, 90, 180, 270]

s1 = Screen()
tom = Turtle()

turtle.colormode(255)
tom.width(10)
tom.shape("turtle")
tom.speed("fastest")

for _ in range(100):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    # tom.setheading(random.randrange(0, 360, 90))
    tom.setheading(random.choice(direction))
    tom.pencolor((r,g,b))
    tom.forward(30)


s1.exitonclick()