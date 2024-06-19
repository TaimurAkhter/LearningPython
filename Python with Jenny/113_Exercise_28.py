# ----------Date: 12th February 2024 Monday
# -------Time : 06 : 39 PM

# Now Start Time : 07 : 03 PM
# End Time : 07 : 43 PM
from turtle import Turtle, Screen
s1 = Screen()
line = Turtle()

line.penup()
line.backward(200)
line.pendown()

def dashes():
    line.forward(10)
    line.penup()
    line.forward(10)
    line.pendown()

color = ["red", "violet", "green", "blue", "pink", "orange", "skyblue", "gray", "purple", "darkgreen"]
# print(len(color)) # 10
for i in range(20):
    if i<=9:
        line.pencolor(color[i])
    else:
        line.pencolor(color[i%10]) # Mera matlab hy ky jitni color wali list ki length (10) hy us sy divide kr ky remainder ly lo.
    dashes()

s1.exitonclick()