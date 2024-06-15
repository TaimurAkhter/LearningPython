# Date: 03 December 2023 Sunday
# Time: 07 : 55 PM
# Today Mamoon, Azka and Rauf have reached

# disjoint means both sets not contain same elements

set1 = {"Mamoon", "Rauf", "Azka"}
set2 = {"Tamoor", "Awais", "Akhter", "Salma"}

# print(set1.isdisjoint(set2)) # True
# print(set1.isdisjoint(["Akhter", "Salma", "Mamoon", "Tamoor"]))

#-------------Definitions
# set1 is subset of set2 if every element of set1 is in set2
# set1 is superset of set2 if set1 contains every element of set2

set1 = {"Mamoon", "Rauf", "Azka"}
set2 = {"Tamoor", "Awais", "Akhter", "Salma", "Mamoon", "Rauf", "Azka"}

print(set1.issubset(set2)) # True
print(set1 <= set2) # True


print(set1.issuperset(set2)) # False
print(set2 >= set1) # True

print(set2.issuperset(["Azka", "Mamoon", "Rauf"])) # True


set3 = {"Tamoor", "Akhter", "Salma"}

# clear() delete set items
set3.clear()
print(set3)

# del delete entire set
del set3
print(set3)

# Time: 08 : 10 PM