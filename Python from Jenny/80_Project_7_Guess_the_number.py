# Date: 6th January 2024 Saturday
# Start Time: 10 : 08 PM
# End Time: 11 : 14 PM

import random

print("let me think of a number between 1 to 50.")
level = input("Choose level of difficulty... Type 'easy' or 'hard': ")
if level=="easy":
    lives = 10
elif level=="hard":
    lives = 5
    
random_number = random.randint(1,50)
repeat = True
while repeat:
    print(f"You have {lives} attempts remaining to guess the number!")
    guessed_number = int(input("Make a guess: "))
    if guessed_number == random_number:
        print(f"Your guess is right..The answer was {random_number}")
        break
    elif guessed_number > random_number:
        print("Your Guess is Too High")
    elif guessed_number < random_number:
        print("Your Guess is Too Low")
    if guessed_number != random_number:
        lives -= 1

    if lives == 0:
        print("You are out of guesses.. You lose!!")
        repeat = False