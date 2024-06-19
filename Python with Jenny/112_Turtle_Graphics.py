# -------------Date: 11th February 2024 Sunday
# -------------Start Time : 09 : 59 AM

# -------------Date: 12th February 2024 Monday
# ----------Time : 05 : 01 PM
# ----------End Time: 06 : 39 PM
from turtle import Turtle, Screen
s1 = Screen()
tom = Turtle()
tom.shape("turtle")

#---------------------------------------
# tom.pencolor("red")
# tom.fillcolor("skyblue")
# tom.color("pencolor", "fillcolor")
#---------------------------------------

# tom.color("orange", "green")
# tom.pensize(2)

# tom.begin_fill()
# tom.circle(100)
# tom.end_fill()
# tom.right(90)

# tom.penup()
# print(tom.isdown())
# tom.forward(100)
# tom.pendown()

# tom.pensize(3)
# tom.hideturtle()
# print(tom.isvisible())

# tom.color("green", "orange")
# tom.begin_fill()
# tom.circle(50)
# tom.end_fill()
# print(tom.position())
# tom.goto(-150, -100)

#-----------4 Shapes----------
# tom.speed(10)
tom.penup() # 1st distance
tom.back(150)
tom.left(90)
tom.forward(150)
tom.right(90)

tom.pendown()
tom.pencolor("orange") # ---------------Circle
tom.circle(50)

tom.penup() # 2nd distance
tom.fd(150)
tom.pendown()

tom.pencolor("blue") # -----------Square
tom.forward(80)
tom.left(90)
tom.forward(80)
tom.left(90)
tom.forward(80)
tom.left(90)
tom.forward(80)

tom.penup()
tom.fd(150) # 3rd distance
tom.pendown()
tom.left(90)

tom.pencolor("green") # ---------Pentagon
tom.forward(70)
tom.left(72)
tom.forward(70)
tom.left(72)
tom.forward(70)
tom.left(72)
tom.forward(70)
tom.left(72)
tom.forward(70)
tom.left(72)

tom.penup()
tom.left(180) # 4th distance
tom.forward(100)
tom.pendown()

tom.pencolor("red") # -----------Triangle
tom.forward(100)
tom.right(120)
tom.forward(100)
tom.right(120)
tom.forward(100)
tom.hideturtle()


# ----Road-----
# l1 = Turtle()
# l1.shape("turtle")
# l2 = Turtle()
# l2.shape("turtle")
# track = Turtle()
# track.shape("triangle")

# l1.pensize(2)
# l1.color("black", "skyblue")
# l1.left(90)
# l1.forward(200)

# l2.pensize(2)
# l2.color("black", "skyblue")
# l2.penup()
# l2.forward(50)
# l2.pendown()
# l2.left(90)
# l2.forward(200)

# # track.width(2) # it also works as pensize
# track.color("black", "red")
# track.penup()
# track.forward(25)
# track.pendown()
# track.left(90)
# for i in range(10):
#     track.pendown()
#     track.forward(10)
#     track.penup()
#     track.forward(10)


s1.exitonclick()
# s1.mainloop()
# tom.screen.mainloop()

