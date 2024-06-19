# Date: 05 December 2023 Monday
# Time: 07 : 23 PM
# Now Starting Time: 07 : 46 PM

heights = input("Enter all height separated by a space:")
height_list = heights.split(" ")

count = 0
for i in height_list:
   count = count + 1

# for i in range(count):
#    height_list[i] = int(height_list[i])
# print(height_list[i])
   
sum = 0
for i in height_list:
    sum += int(i)

avg = sum/count
print(avg)
print(round(avg))

# End Time: 08 : 22 PM