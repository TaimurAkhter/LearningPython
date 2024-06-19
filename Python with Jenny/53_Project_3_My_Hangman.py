# Date: 13th December 2023 Wednesday
# Time: 04 : 38 PM

# Date: 14th Dec 2023
# Start Time: 06 : 53 PM
import hangman_stages
print("Let's Play Hangman!!")

# word = input("Enter 6 letters word to guess:"); 
# word.lower()
player1 = "taimur"
# player1 = ["t", "a", "i", "m", "u", "r"]
# --------Make blank list
blank_list = []
for i in range(0, 6):
    blank_list.append("_")
    # player1.append(word[i])

lives = len(player1)
print(f"You have only {lives} so try to guess the word within {lives} attempts! Good luck !!")
print(blank_list)

guess = input("Guess a letter: ")
guess.lower()
loop = True
while loop:
    if guess in player1:
        index = player1.index(guess)
        blank_list.pop(index)
        blank_list.insert(index, guess)
        print(blank_list)
        print(hangman_stages.stages[lives])
    else:
        print("Your guessed letter is not present in the word.So you lose a life")
        print(blank_list)
        lives -= 1
        print(hangman_stages.stages[lives])

    if lives == 0:
        print("You Lose")
        loop = False
    elif blank_list == player1:
        print(hangman_stages.stages[lives])
        print("You win!")
        loop = False
    else:
        guess = input("Guess a letter: ")
