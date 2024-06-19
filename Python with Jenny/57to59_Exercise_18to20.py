# Date: 18th Dec 2023 Monday
# Start Time: 10 : 30 PM

# Search : python reeborg hurdle (1 , 2 , 3 and 4)
# Python reeborg hurdle 4
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
'''
# Python reeborg hurdle 3
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
'''       
# Python reeborg hurdle 2
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    jump()
'''
# Python reeborg hurdle 1 put in hurdle 2 instead while loop
# for i in range(6):
#     jump()

# End Time: 10 : 41 PM