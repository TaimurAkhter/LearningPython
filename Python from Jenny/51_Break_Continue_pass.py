# Date: 12 December 2023 Tuesday
# Time: 04 : 17 PM
# Time: 06 : 07 PM
# Start Time: 07 : 31 PM

# ------Loop control statements break,continue,pass

# -------------break with while loop
# count = 1
# while count <= 10:
#     print(count)
#     count += 1
#     if count == 7:
#         break
#     print("Hi")
# print("out from loop")

# ------------break with nested for loop
# list1 = ["Hi","Hey","Welcome"]
# names = ["Awais","Mamoon","Taimur"]

# for item in list1:
#     for name in names:
#         print(item, name)
#         if item == "Hey" and name == "Awais":
#             break
#     print("out from inner loop")
# print("out from outer loop")
    
# ------------continue with while loop
count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 7:
        pass
    print("Hi")
print("out from loop")

# ------------continue with for loop
# for i in range(1, 11):
#     if i==7:
#         continue
#     else:
#         print(i)
        
# ------------Pass
# for i in range(1, 11): # It will give error

for i in range(1, 11):  # It will not give error
    pass

