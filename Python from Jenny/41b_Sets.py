# Date: 23 Nov 2023 Wednesday
# Time: 04 : 21 PM
# 05 : 11 PM ty azaan hoi

# X.union(), X.intersection() method argument is iterable it can be list, dict, tuple etc. 
# It will convert it into set then perform union,intersection on that iterable
# union |
# For |, |=, & operators All operands should be set

set1 = {"Tamoor", "Mujeeb", "Salma", "Akhter",          "Haseeb"}
set2 = {                    "Salma", "Akhter", "Awais", "Haseeb", "Mamoon"}
set3 = {"Tamoor", "Mujeeb", "Salma", "Akhter", "Awais",           "Rauf"}

# print(set1.union(set2, set3))
# print(set1 | set2 | set3)


# print(set1.union(["Salma", "Mujeeb"]))
# print( set1.union(set2, ("Almas", "Haseeb") )) 

# print(set1 | set3 | ("Rauf", "Mujeeb"))   # Error

# You can Update the set
# set4 = {"Awais", "Salma"}
# set1.update(set4)
# set1 |= set4

# set1.update(["Awais", "Salma"])
# set1 |= ["Awais", "Salma"]        # Error
# print(set1)


# print(set1.intersection(set2, set3)) # {'Salma', 'Akhter'}
# print(set2.intersection(["Awais", "Haseeb", "Tamoor", "Rauf"]))

# print(set2 & set3)

set1.intersection_update(set3)
print(set1) # {'Mujeeb', 'Salma', 'Tamoor', 'Akhter'}

# End Time: 10 : 21 PM

# End Time: 10 : 25 PM