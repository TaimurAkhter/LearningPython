# Date: 6th January 2024 Saturday
# Start Time: 11 : 22 PM
# End Time: 11 : 50 PM

import random,os
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5
def set_difficulty(level_chosen):
    if level_chosen==0:
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen==1:
        return HARD_LEVEL_ATTEMPTS
    else:
        return

def check_answer(guessed_number,answer,attempts):
    if guessed_number > answer:
        print("Your Guess is Too High")
        return attempts-1
    elif guessed_number < answer:
        print("Your Guess is Too Low")
        return attempts-1
    else:
        print(f"Your guess is right..The answer was {answer}")
        
def game():
    print("let me think of a number between 1 to 50.")
    answer = random.randint(1,50)
    print(answer)
    level = int(input("Choose level of difficulty... Type '0' easy or '1' hard: "))
    attempts = set_difficulty(level)
    if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
        os.system('cls')
        print("You have entered wrong difficulty level..Play again!!")
        game()

    guessed_number = 0
    while guessed_number!=answer:
        print(f"You have {attempts} attempts remaining to guess the number!")
        guessed_number = int(input("Make a guess: "))
        attempts = check_answer(guessed_number,answer,attempts)
        if attempts == 0:
            print("You are out of guesses.. You lose!!")
            return
        elif guessed_number != answer:
            print("Guess again")
game()

