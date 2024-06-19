# 3rd Nov 2023 Friday
# Time : 05 : 29 PM

# Write a program that generate random number either 0 or 1 and based on that you can tell heads or tails. 0 means tails and 1 means heads.
import random
random_number = random.randint(0,1)
print(random_number)
if random_number == 1:
    print("Heads")
else:
    print("Tails")