# 28th Oct 2023 Saturday
# Time 10 : 00 PM 

# a = 10
# b = 10
# print(id(a))
# print(id(b))
# print(a is b) # True
# print(a is not b) # False

c = 7
d = 7
print("1st id of c ", id(c))
print("id of d ", id(d))
print("c is d: ", c is d) # True
print("c is d: ", c is not d) # False

c = 8
print("2nd id of c ", id(c))

print("c is d: ", c is d) # False
print("c is d: ", c is not d) # True

# Coding Exercise
print("c is c: ", c is c) # True

# Time 10 : 28 PM 