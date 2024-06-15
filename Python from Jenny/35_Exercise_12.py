# 3rd Nov 2023 Friday
# Time : 05 : 53 PM

# Write a program which will select a random name from a list of names & the person selected will have to pay for everybody's food bill
import random
# without random.choice()

names = input("Enter everybody's name separated by comma:")
names_list = names.split(",")
index = random.randint(0, len(names_list)-1)

# person = random.choice(li)
print(f"{names_list[index]} will pay the bill")