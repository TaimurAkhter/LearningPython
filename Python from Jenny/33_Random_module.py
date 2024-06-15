# 3rd Nov 2023 Friday
# Time : 05 : 14 PM
import random

l = [1, 6, 12, 13, 44]

# a = random.randint(1, 9) # (a <= X <= b)
# a = random.randrange(1, 9) # (a <= X < b)

# random generates float number only between 0 and 1
# a = random.random()

# uniform generates float number between given values i.e 1 and 2
# a = random.uniform(1, 2)

# Generates random items from i.e. list 
# a = random.choice(l)

# print(a)

# a = random.shuffle(l) # None because it does not return the list

random.shuffle(l)
print(l)

# Time : 05 : 27 PM