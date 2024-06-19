# Date: 11 December 2023 Monday
# Start Time: 07 : 19 PM

# 12mint 20sec assignment in video: In below in while loop if count<1 then what should it print
count = 1
while count <= 5:
    print(count)
    count += 1
    # if count == 3: 
    #    break
else: 
    print("in else block")
print("Out from loop")

# If you don't know how many times the loop would be executed, so what condition you will put here and when the loop would be terminated, how you will terminate the loop. So in this type of situation we provide a special value which is called sentinel. It is a special value which is used to terminate the loop. 
# 22 mint 9second per Urdu boli

# number = int(input("Enter a number(-1 to quit)"))
# Here -1 or anything is a special value or a sentinel value.
# while number != -1:
#     print(number)
#     number = int(input("Enter a number(-1 to quit)"))
# else:
#     print("in else block")
# print("Out from loop")

# count = 0
# while True:
#     print(count)
#     count += 1
#     if count == 5:
#         break
# else:
#     print("in else block")
# print("Out from loop")

input_val = int(input("Enter a number for sum: "))
num = input_val
total = 0
while input_val != 0:
    total += input_val
    input_val = int(input("Enter a number for sum: "))
print("Total is ", total)

# Date: 12 December 2023 Tuesday
# End Time: 04 : 14 PM