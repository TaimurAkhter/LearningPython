# Date: 10 December 2023 Sunday
# Start Time: 06 : 18 PM
# Today Me and mama went to 205 at 01:30 PM. We came back to home at 04:00 PM.
# Project: Password Generator

import random

# num = random.randint(1, 5)
# num = random.randrange(1, 5)
print("Welcome to Password Generator!")

# letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

# Stop at: 06 : 28 PM I am going to eat dinner
# Time: 07 : 42 PM 
# Now I come back. 
# In this time I eat dinner, clean store and clean motorcycles(Prider and CD70).

# How many letters,numbers and symbols user need?
need_letters = int(input("How many letters would you like in your password?\n"))
need_numbers = int(input("How many numbers would you like?\n"))
need_symbols = int(input("How many symbols would you like?\n"))

# -------generating random letters-----
str1 = ""
for i in range(0, need_letters):
    random_index = random.randrange(0, 52)
    str1 += f"{letters[random_index]} "     # convert random letters with a space into string
# print(str1)

  
# -------generating random numbers---------
str2 = ""
for i in range(0, need_numbers):
    random_index = random.randrange(0, 10)
    random_number = str(numbers[random_index])
    str2 += f"{random_number} "             # convert random numbers with a space into string
# print(str2)

# -------generating random symbols---------
str3 = ""
for i in range(0, need_symbols):
    random_index = random.randrange(0, 10)
    str3 += f"{symbols[random_index]} "     # convert random symbols with a space into string
# print(str3)


# Combine all the strings into one string
combine = str1 + str2 + str3

# We separated the element of the strings with a space, 
# It is helpful to convert the string into list by split(" ") function

# Now Convert the combine string into list by split()
list = combine.split(" ")
list.pop() # At the end of the string has a space, so in list we remove space that lies at end
# print(list)

# Date: 11th Dec 2023  Time: 04 : 43 PM
# s_p = ""
# for i in range(0, len(list)):
#     s_p += list[i]
# print(f"This is a simple password is {s_p}\n")
#-----11th Dec 2023  Time: 04 : 43 PM---

# Now shuffle the list to generate random password
random.shuffle(list)

# Final step: Make an empty string. Run for loop with list to take all elements of list one-by-one.
random_password = ""
# All the element of the list are strings.
for i in range(0, len(list)):
    # combine the elements of list in empty string (line 65 => random_password) that you create.
    random_password += list[i]
# Now the password is Ready
print(random_password)

# Now the End Time is: 09 : 40 PM
# Date: 10th December 2023 Sunday