# ----------Date: 9th February 2024 Friday
# ------Time : 02 : 00 PM
# ------Time : 02 : 03 PM 

# Date: -----------10th February 2024 Saturday

# -------Start Time : 10 : 07 PM

# -------------Date: 11th February 2024 Sunday
# -------------Start Time : 08 : 43 AM
# -------------End Time : 09 : 58 AM
'''
Aaj mein 07:37 AM pr jaga 
'''
import turtle
# turtle.getscreen()

# There are 6 Shapes : "circle", "turtle", "arrow", "square", "classic", "triangle"
turtle.shape("arrow")
print(turtle.shape()) # It shows what shape you use.

# If input is a number greater than 10 or smaller than 0.5, speed is set to 0. Speed-strings are mapped to
# speed-values as follows:
# "fastest": 0
# "fast": 10
# "normal": 6
# "slow": 3

# ---Square
turtle.speed(5)
turtle.forward(100)
turtle.left(90) # use left or lt function
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.circle(100)
# turtle.circle(100,350,9)

# ---Rectangle
# turtle.forward(150)
# turtle.left(90)
# turtle.forward(70)
# turtle.left(90)
# turtle.forward(150)
# turtle.left(90)
# turtle.forward(70)

# ---Triangle
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)

# turtle.right(100)
# turtle.rt(100)

turtle.exitonclick()
# turtle.done()
# turtle.mainloop()
