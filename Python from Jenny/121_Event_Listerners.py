# Date: 28th February 2024 Tuesday
# Now Time 10 : 00 AM

# Today is party of 10th class by our class 9th
# Aaj takriban 8:20AM pr mein mama nu station ty cho-rny gya wapsi pr mein ny school jana tha mujy party ka time nahi pata tha.        Jab mein wapis a raha tha tu mujy aik classfellow mila us ny sir sy pocha or mujy bataya ky 12:30PM pr jana hy. Is tarha mera chakar bach gya or mein ghar agya. phir mein ny computer chalaya thori der baad light chli gai approximately 08:52AM pr. Phr mein ny chemistry ka tesra 3rd chapter parha usky bs last 3 page rah gaye wo mein ab computer jab bnd kro ga tb parho ga.

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