# ----------Date: 12th February 2024 Monday
# -------Time : 06 : 39 PM # Abu aye advocate nu paisy dy ky

# Now I am going to eat dinner Time : 06 : 40 PM

# Time : 07 : 00 PM Hn mein aya waan. Pehlay mein chota mug pani da rakhaya si Abu ny chadar wisha li si ty wada mug pani da rakh lya si pehlay. Phir mein rotian layandian phir mama ny salan lyanda alu palak pakai si. Khana kha ky mein pehlay rotian bathal ch sitian phir mein bartan chukay. Phir mein choti motor cycle CD 70 Saf kiti. Phir Hn Hand wash kr ky aya si.

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