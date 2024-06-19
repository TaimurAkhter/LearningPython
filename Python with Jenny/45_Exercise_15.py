# Date: 05 December 2023 Monday
# Time: 08 : 23 PM

# Program to find maximum number from a list of numbers

numbers = input("Enter numbers separated with space:")
list = numbers.split(" ")

# Convert all strings to integer
for i in range(0, len(list)):
    list[i] = int(list[i])

# print(max(list))
maximum_number = 0

for i in list:
    if(i > maximum_number):
        maximum_number = i

print(f"The maximum number is {maximum_number}")

# End Time: 09 : 16 PM