# Date: 8th January 2024 Saturday
# Start Time: 07 : 49 AM

import random,os
import Project_8_database
import Project_8_Text

def compare(name):
    return f"{name['name']}, a {name['description']}, from {name['country']}"

def check(name1_F, name2_F, followers): #1
    name1_F = name1_F['follower_count'] # 1000
    name2_F = name2_F['follower_count'] # 600
    if followers == 1:
        if name1_F > name2_F:
            return True
        else:
            return False
    elif followers == 2:
        if name2_F > name1_F:
            return True
        else:
            return False
        
score = 0
print(Project_8_Text.game_logo)
name2 = random.choice(Project_8_database.data)

continue_flag = True
while continue_flag:

    name1 = name2
    name2 = random.choice(Project_8_database.data)
    while name1==name2:
        name2 = random.choice(Project_8_database.data)

    print(f"Compare 1: {compare(name1)}")
    print(Project_8_Text.vs)
    print(f"Compare 2: {compare(name2)}")

    choose = int(input("Who has more followers? Type '1' or '2': "))
    followers = check(name1,name2,choose)

    os.system('cls')
    print(Project_8_Text.game_logo)
    if followers:
        score += 1
        print(f"You are right. Your score is {score}")
    else:
        print(f"You are wrong. Your final score is {score}")
        continue_flag = False
