###----------Today is 3rd February 2024 Saturday 
###----------Time 10 : 39 PM Till Now I watch 20 videos Today
###----------Time 10 : 40 PM Now I am shutting down the computer

#----------Today is 4th February 2024 Sunday 
###----------Time 12 : 16 PM Now I complete this Tutorial 21

# def average(a, b, c=1):
#     print("The average is ", (a + b + c) / 2)

# As a tuple
def average(*numbers):
    # print(type(numbers)) # <class 'tuple'>
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is: ", sum / len(numbers))
    return sum / len(numbers)

# average(4,6)
c = average(5, 6, 7, 1)
print(c)

# As a dictionary
# def name(**name):
#     print(type(name)) # <class 'dict'>
#     print("Hello", name["fname"], name["mname"], name["lname"])

# name(fname = "M.", mname = "Akhter", lname = "Javed Sandhu")

# def returnF(fname, mname, lname):
#     return "Famous " + fname + " " + mname + " " + lname 
# print(returnF("Carry", "On", "Jatta 3"))

# CodeWithHarry Example
# def name(fname, mname = "Akhter", lname = "Sandhu"):
#     print("Hello," , fname, mname, lname)
# name("Taimur")
