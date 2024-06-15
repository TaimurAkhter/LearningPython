# Date: 10th January 2024 Saturday
# Start Time: 07 : 16 PM
# End Time: 08 : 53 PM

import random
import os
import Project_8_database
import Project_8_Text

def display_accountInfo(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def  check_answer(guess,followers_1,followers_2):
    if followers_1<followers_2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
            return False

score = 0
print(Project_8_Text.game_logo)
account_2 = random.choice(Project_8_database.data)

continue_flag = True
while continue_flag:
    account_1 = account_2
    account_2 = random.choice(Project_8_database.data)
    
    while account_1==account_2:
        account_2 = random.choice(Project_8_database.data)

    print(f"Compare 1: {display_accountInfo(account_1)}")
    print(Project_8_Text.vs)
    print(f"Compare 2: {display_accountInfo(account_2)}")

    guess = int(input("Who has more followers? Type '1' or '2': "))
    follower_count_1 = account_1["follower_count"]
    follower_count_2 = account_2["follower_count"]

    is_correct = check_answer(guess,follower_count_1,follower_count_2)
    os.system('cls')
    print(Project_8_Text.game_logo)
    if is_correct:
        score += 1
        print(f"You are right. Your score is {score}")
    else:
        print(f"You are wrong. Your final score is {score}")
        continue_flag = False
