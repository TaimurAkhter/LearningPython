# Date: 11th December 2023 Monday
# End Time: 07 : 11 PM
# Project: Password Generator

import random
print("Welcome to Password Generator!")
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"
# How many letters,numbers and symbols user need?
need_letters = int(input("How many letters would you like in your password?\n"))
need_numbers = int(input("How many numbers would you like?\n"))
need_symbols = int(input("How many symbols would you like?\n"))

# -------generating random letters,numbers and symbols-----
list = []
for i in range(0, need_letters):
    random_index = random.randrange(0, 52)
    list.append(letters[random_index]) # Append random elements of string into list

for i in range(0, need_numbers):
    random_index = random.randrange(0, 10)
    list.append(str(numbers[random_index]))   

for i in range(0, need_symbols):
    random_index = random.randrange(0, 10)
    list.append(symbols[random_index])
# print(list)
random.shuffle(list)
# Converting elements of list into string
password = ""
for i in range(0, len(list)):
    password += list[i]
print(password)