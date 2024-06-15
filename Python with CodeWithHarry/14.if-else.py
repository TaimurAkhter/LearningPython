# If else Conditional Statements in Python
# a = int(input("Enter your age: "))
# print("Your age is: ", a)
# Conditional Operators
# >, <, >=, <=, ==, !=
# print(a < 18)
# print(a <= 18)
# print(a == 18)
# print(a != 18)

# if (a > 18):
#     print("Yes")
#     print("You can drive")
# else: 
#     print("No")
#     print("You cannot drive")

# print("okay")

#--------------------------------

# bike = int(input("Bike CC: "))

# ltre1 = 263
# rupees = int(input("Enter Your Amount: "))
# litres = rupees // ltre1

# if bike == 70:
#     print("Your Bike can run about ", litres * 55, " km")
# elif bike == 100:
#     print("Your Bike can run about ", litres * 50, " km")
# else:
#     print("You have not enough petrol")

question = "My name is :___?\n"
points = "0/1\n"
op1 = 'a)Tamoor\n' 
op2 = 'b)Taimur\n' 
op3 = 'c)Ali' 
print(question,points,op1,op2,op3)
ans = input("Enter answer:")


match ans:
    case _ if ans == "b":
        print("You scored 100% marks")
        p = 1
        for i in range(p):
            i += 1
        print("You scored ",i,"/1 marks")
    case _:
        print("You scored 1/0 marks")

###----------Today is 3rd February 2024 Saturday
# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)