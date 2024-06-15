# -----Date: 15th February 2024 Thursday
# -----Start Time : 01 : 39 PM
# Time : 02 : 30 PM -- Mama nu lein gya si
# Continue Time : 04 : 12 PM
# takriban 05:15 PM Badminton khalyn lag gaye si 15 20 mint
# ----- End Time : 07 : 34 PM

from turtle import Turtle, Screen
import random
s1 = Screen()

def players():
    no_of_turtles = int(input("How many turtles you want to race(2-10):"))
    if no_of_turtles >= 2 and no_of_turtles <= 10:
        return True, no_of_turtles
    else:
        print("Invalid Input")
        return False, False

okay, count = players()
n1 = 0
n2 = 1
# ----------------Finish Line
Finish_Line = Turtle()
Finish_Line.speed(10)
Finish_Line.hideturtle()
Finish_Line.penup()
Finish_Line.left(90)
Finish_Line.forward(250)
Finish_Line.pendown()
Finish_Line.left(90)
Finish_Line.forward(330)
Finish_Line.left(180)
Finish_Line.forward(600)
# -----------------

turtle_color = ["red", "pink", "orange", "blue", "green", "skyblue", "gray", "brown", "darkblue", "purple"]
speed = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5]

turtle_list = []
for i in range(count):
        FD = 60 * n1
        BK = 60 * n2
        tom = Turtle()
        tom.shape("turtle")
        tom.color(turtle_color[i])
        tom.penup()
        tom.speed(10)
        if i==0 or i==2 or i==4 or i==6 or i==8:
            tom.forward(FD)
            n1 += 1
        if i==1 or i==3 or i==5 or i==7 or i==7 or i==9:
            tom.backward(BK)
            n2 += 1
        tom.left(90)
        tom.backward(150)
        tom.pendown()

        turtle_list.append(tom)
# print(Finish_Line.position()) # (270.00,250.00)

# Only write this concept from solution
is_race_on = True
while is_race_on:
    for i in turtle_list:
        distance = random.randrange(5, 20)
        
        i.forward(distance)
        i.penup()
        i.forward(distance)
        i.pendown()
        x,y = i.position()
        if y>=250:
            print(f"Winner is {i.pencolor()} turtle")
            is_race_on = False
            break

s1.exitonclick()

#-----------------Jenny--------Solution
# HEIGHT,WIDTH = 400,400
# color_list = ["red", "pink", "orange", "blue", "green", "skyblue", "gray", "brown", "darkblue", "purple"]

# def no_of_turtle():
#     count = 0
#     while True:
#         count = int(input("How many turtles you want to race(2-10):"))
#         if 2<=count<=10:
#             return count
#         else:
#             print("Input is not in given range...Try again!!")
            
# turtles = no_of_turtle()
# # print(turtles)

# s1 = Screen()
# s1.setup(400,400)

# x_spacing = 400//(turtles+1)

# turtle_list = []
# for i in range(1, turtles+1):

#     new_turtle = Turtle()
#     new_turtle.shape("turtle")
#     new_turtle.left(90)
#     new_turtle.color(color_list[i-1])
#     new_turtle.penup()
#     new_turtle.goto(-WIDTH//2 + (i*x_spacing), -HEIGHT//2 + 10)
#     #               -400//2 + (1*100)
#     turtle_list.append(new_turtle)

# def race():
#     is_race_on = True
#     while is_race_on:
#         for i in turtle_list:
#             distance = random.randrange(5, 20)
#             i.forward(distance)

#             x,y = i.position()
#             if y>=HEIGHT//2:
#                 print(f"Winner is {i.pencolor()} turtle")
#                 is_race_on = False            

# race()

# s1.exitonclick()