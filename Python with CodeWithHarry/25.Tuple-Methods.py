# countries = ("Spain", "Italy", "Romania", "Germany", "England")
# temp = list(countries)
# temp.append("Russia")
# temp.pop(3)
# temp[2] = "Finland"
# temp.insert(2, "France")
# countries = tuple(temp)
# print(countries)

Tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = Tuple1.count(3)
res = Tuple1.index(3, 4, 8)
print("Count of three in Tuple1 is: ", res)



