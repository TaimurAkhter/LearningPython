# 6th Nov 2023 Monday today khala shado has gone back to home in Saraich at takri ban 01 : 30 PM 
# Time : 07 : 18 PM
# 8th Nov 2023 Wednesday Before Drawing Time : 05 : 59 PM --> Now 06 : 00 PM

import random

user_input = int(input("Enter your Choice: Type 0 for Rock, 1 for Paper, 2 for Scissors."))
if user_input >= 3 or user_input < 0:
    print("You entered invalid number.")
else:    
    computer_choice = random.randint(0,2)
    print("Computer Choose:")
    print(computer_choice)

    if user_input == computer_choice:
        print("Its a Draw")
    elif computer_choice == 2 and user_input == 0:
        print("You Win")
    elif computer_choice == 0 and user_input == 2:
        print("You lose")
    elif computer_choice > user_input:
        print("You lose")
    elif user_input > computer_choice:
        print("You Win")
    else:
        print("Invalid Input")

# 8th Nov 2023 Wednesday Now Time : 06 : 27 PM We are going to Sharif Town
# And Computer is shut down