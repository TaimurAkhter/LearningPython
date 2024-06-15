tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90

print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[32])

if 76 in tup:
    print("Yes")
tup2 = tup[1:4]
print(tup2)