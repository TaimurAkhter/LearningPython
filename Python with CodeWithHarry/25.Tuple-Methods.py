countries = ("Spain", "Italy", "Romania", "Germany", "England")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
temp.insert(2, "France")
countries = tuple(temp)
print(countries)

Tuple1 = (0, 1, 2, 9, 2, 31, 1, 3, 2, 3)
res = Tuple1.count(3)
print("Count of three in Tuple1 is: ", res)

# ---------tuple.index(element, start, end)-------
res = Tuple1.index(31, 4, 8) # 8-1 = 7
print("Index of 31 in Tuple1 between index 4 to 7 is: ", res)
res = Tuple1.index(9)
print("Index of 9 in Tuple1 is: ", res)

