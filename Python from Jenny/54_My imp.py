# Date: 15th Dec 2023
# End Time: 07 : 27 PM
import hangman_stages
print("Let's Play Hangman!!")

player1 = "taimur"

blank_list = []
for i in range(0, 6):
    blank_list.append("_")

lives = 6
print(f"You have only {lives} so try to guess the word within {lives} attempts! Good luck !!")
print(blank_list)

loop = True
while loop:
    guess = input("Guess a letter: ").lower()
    for index in range(len(player1)):
        letter = player1[index]
        if letter == guess:
            blank_list[index] = guess
    print(blank_list)

    if guess not in player1:
        lives -= 1
        if lives == 0:
            loop = False
            print("You lose!!")
    if "_" not in blank_list:
        loop = False
        print("You win!!")
    print(hangman_stages.stages[lives])