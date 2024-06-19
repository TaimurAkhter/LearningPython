# ----------Date: 13th February 2024 Tuesday
# ------Start Time : 01 : 25 PM
# -----------------------------Time : 01 : 41 PM Khapaya
# -----End Time : 02 : 03 PM

from turtle import Turtle, Screen
s1 = Screen()
arrow = Turtle()

color = ["red", "violet", "green", "blue", "pink", "orange", "skyblue", "gray", "purple", "darkgreen"]
for i in range(3, 9): # 0 1 2 3
    angle = 360/i
    arrow.pencolor(color[i%10])
    for _ in range(i):
        arrow.forward(100)
        arrow.right(angle)

s1.exitonclick()




#---------------------Khapaya
# arrow.penup()
# arrow.forward(70)
# arrow.pendown()

# arrow.speed(1)
# arrow.right(120)
# arrow.forward(70)
# arrow.right(120)
# arrow.forward(70)
# arrow.right(120)
# arrow.forward(50)
# sides = 3
# for i in range(2): # 0 1 2 3
#     n1 = sides+i
#     a = 360/n1
#     arrow.right(a)
#     arrow.forward(50)
#     arrow.right(a)
#     arrow.forward(50)
#     arrow.right(a)
#     arrow.forward(50)
# arrow.right(a)