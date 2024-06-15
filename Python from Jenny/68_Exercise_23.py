# Date: 4th January 2024 Thursday
# Start Time: 10 : 31 PM
# End Time: 10 : 55 PM

marks_dict = {
    'Taimur': 94,
    'Awais' : 100,
    'Mamoon': 100,
    'Hamza' :84,
    'Mazhar': 84,
    'person1': 57,
    'person2': 47,
    'person3': 40
}

# for i in marks_dict.items():
#     if i[1] >= 91:
#         marks_dict[i[0]] = "A+"
#     elif i[1] >= 81:
#         marks_dict[i[0]] = "A"
#     elif i[1] >= 71:
#         marks_dict[i[0]] = "B+"
#     elif i[1] >= 61:
#         marks_dict[i[0]] = "B"
#     elif i[1] >= 51:
#         marks_dict[i[0]] = "C"
#     elif i[1] >= 41:
#         marks_dict[i[0]] = "D"
#     else:
#         marks_dict[i[0]] = "F"

# print(marks_dict)

# Jenny Solution
grades = {}
for i in marks_dict:
    num = marks_dict[i]
    if num > 91:
        grades[i] = "A+"
    elif num > 81:
        grades[i] = "A"
    elif num > 71:
        grades[i] = "B+"
    elif num > 61:
        grades[i] = "B"
    elif num > 51:
        grades[i] = "C"
    elif num > 41:
        grades[i] = "D"
    else:
        grades[i] = "F"

print(grades)