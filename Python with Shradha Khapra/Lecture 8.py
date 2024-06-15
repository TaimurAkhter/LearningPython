# Date: 21st February 2024 Wednesday
# Start Time: 01 : 39 PM
# Code Writing Time: 01 : 54 PM
# Time : 02 : 29 PM

# Continue Time : 04 : 30 PM
# End Time: 04 : 42 PM


"""
Class & Instance Attributes:
    Class.attr  # class attr access with obj name or Class name
    obj.attr    # object attr access with obj name

MCQ:
1. There are two types of constructors:
    i) default constructor          # Blank means there is nothing in constructor. 
    ii) parameterized constructor
    
2. Every time when you create object of class then __init__ function is called either it is created or not.
3. When there is same value of class attr and obj attr than always obj attr got higher precedence or priority.
"""

class Student:
    college_name = "ABC college"    # Class Attribute
    # parameterized constructor
    def __init__(self, name, marks):
        self.name = name    # Object Attribute
        self.marks = marks

    def welcome(self):
        print("Welcome,", self.name)
    def get_marks(self):
        return self.marks

# s1 = Student("Tamoor", 100)
# print(s1.college_name)
# print(Student.college_name)

# s1.welcome()
# print(s1.get_marks())

# Let's Practice
# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

# class Student:
#     def __init__ (self, name,marks):
#         self.name = name
#         self.marks = marks
#     def get_average(self):
#         # sum = self.marks[0]+self.marks[1]+self.marks[2]
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "your marks average is", sum/3)

# s1 = Student("tony stark" , [99,98,97])
# s1.get_average()

# s1.name = "Taimur"
# s1.get_average()

# ----------Important----------
# Encapsulation
# Wrapping data and functions into a single unit (object).
    
# Abstraction
# Hiding the implementation details of a class and only showing the essential features to the user.
class Car:
    def __init__ (self):
        self.acc= False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")
          
car1 = Car()
car1.start()

# Let's Practice
# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.
class Account:
    def __init__ (self, bal, acc):
        self.balance = bal
        self.account_no = acc
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = " , self.get_balance())
    
    def credit (self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = " , self.get_balance())
    
    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)
