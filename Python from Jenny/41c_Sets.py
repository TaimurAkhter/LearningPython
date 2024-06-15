# Date: 24 Nov 2023 Wednesday
# Time: 02 : 34 PM
# Time: 02 : 52 PM

set1 = {"Awais", "Mamoon", "Haseeb", "Salma"}
set2 = {"Tamoor", "Akhter", "Awais"}
set3 = {"Salma", "Akhter", "Mamoon"}

# print(set1.union(set2))                 # {'Awais', 'Mamoon', 'Haseeb', 'Salma'}
# print(set1.intersection(set2))          # {'Awais'}
# print(set1.difference(set2))            # {'Mamoon', 'Haseeb', 'Salma'}
# print(set1.symmetric_difference(set2))  # {'Haseeb', 'Tamoor', 'Salma', 'Mamoon', 'Akhter'}


# print(set1.difference(set2))
# print(set2.difference(["Mujeeb", "Salma", "Awais"]))
# print(set1 - set3)

# set1.difference_update(set2)
# set2.difference_update(set3)
# print(set1)
# print(set2)

# print(set1.union(set2) - set1.intersection(set2))

# print(set1.symmetric_difference(set2))    # Note: Takes only one argument
# print(set1 ^ set2 ^ set3)                 # You can Apply with multiple sets with operator (^)

# print(set1.symmetric_difference(set2, set3))      # Error It takes only one argument


set2.symmetric_difference_update(["Salma", "Mamoon"])
print(set2) # {'Akhter', 'Salma', 'Awais', 'Tamoor', 'Mamoon'}


# End Time: 03 : 31 PM