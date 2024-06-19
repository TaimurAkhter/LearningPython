# 6th Nov 2023
# Time : 06 : 02 PM

# row1 = [1, 1, 1]
# row2 = [1, 1, 1]
# row3 = [1, 1, 1]

# num = input("Enter the position where you want to hide money:")

# if num[0] == "1":
#     if num[1] == "1":
#         row1[0] = "X"
#     elif num[1] == "2":
#         row1[1] = "X"
#     else:
#         row1[2] = "X"
        
# elif num[0] == "2":
#     if num[1] == "1":
#         row2[0] = "X"
#     elif num[1] == "2":
#         row2[1] = "X"
#     else:
#         row2[2] = "X"

# else:
#     if num[0] == "3":
#         if num[1] == "1":
#             row3[0] = "X"
#         elif num[1] == "2":
#             row3[1] = "X"
#         else:
#             row3[2] = "X"

# print(f"{row1}\n{row2}\n{row3}")

# Time : 06 : 22 PM

row1 = [1, 1, 1]
row2 = [1, 1, 1]
row3 = [1, 1, 1]

matrix = [row1, row2, row3]
print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
num = input("Enter the position where you want to hide money:")

new_Matrix = matrix[int(num[0])-1]
new_Matrix[int(num[1])-1] = "X"

print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")

# Time : 06 : 28 PM

# After all pangay Time : 07 : 15 PM
# if num=="11" or num=="12" or num=="13" or num=="21" or num=="22" or num=="23" or num=="31" or num=="32" or num=="33":   
#    num = num
# else:
#     num = "33"