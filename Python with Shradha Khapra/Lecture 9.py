# Date: 21st February 2024 Wednesday
# Start Time: 04 : 44 PM


# del keyword
#     Used to delete object properties or object itself.
#     del s1.name
#     del s1

# class Student:
#     def __init__ (self, name):
#         self.name = name

# s1 = Student("shradha")
# print(s1.name)

# del s1.name
# print(s1.name)

# Time: 04 : 49 PM
# 2mint pehlay abu motorcycle ch petrol dilwa ky aye si phir abu kunear da poda dekhan nursery chaly gaye. School wasty chahida si
# Hn mein chat tu aya si Cular dy ky


# Private(like) attributes & methods:
#     Conceptual Implementations in Python:
#       Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # private attr
    
    def my_pass(self):
        print(self.__acc_pass)  # accessing private attr with private class method

acc1 = Account("12345", "abcd")
# print(acc1.acc_no)
# # print(acc1.__acc_pass) # Error
# acc1.my_pass()

# ------------------------------------------
class Person:
    __name = "anonymous"

    def __hello(self): # private method
        print("hello person")

    def welcome(self):
        self.__hello()

p1 = Person()
# # p1.__hello() Error
# p1.welcome()

#---------------Continue---------------------
# Date: 25th February 2024 Sunday
# Time: 02 : 58 PM
# Start Time: 03 : 14 PM
# Start Writing Time: 03 : 32 PM
# Time: 03 : 41 PM Asar di Azan hoi

# class method:
#     A class method is bound to the class & receives the class as an implicit first argument.
#     Note - static method can't access or modify class state & generally for utility.

# If want to access our class directly into method/function then classmethod decorator is used.

class Person:
    name = "Mamoon" # class attribute

    # def changeName(self, name): # In these method first argument is our object.
        # self.name = name
        # self.__class__. something or Person. something
    # The above two ways work.

    @classmethod
    def changeName(cls, name): # cls is not self. This is actually referring to the class
        cls.name = name # This change directly into class attr

    @staticmethod
    def Name():
        print("My name is M. Taimur Akhter")

p1 = Person()
# p1.changeName("Awais")
# print(p1.name)
# print(Person.name)
# p1.Name()

# ----------------In the above we learn what we can do to change class attribute value
# Time: 04 : 04 PM

# There are three types of methods that we learn:
#     1. static methods : use decorator : no takes anything as argument
#     2. class methods  : use decorator : cls argument compulsory       : cls referring to the class
#     3. normal methods : Nothing       : self argument compulsory      : self referring to the object 

# Property:
#   We use @property decorator on any method in the class to use the method as a property.
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage =  str((self.phy + self.chem + self.math) / 3) + "%" # gives same average
    
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

obj = Student(60, 60, 75)
# print(f"Before : {obj.percentage}") # 65.0%
# obj.math = 72
# print(f"After  : {obj.percentage}") # 64.0%

# Date: 25th February 2024 Sunday
# End Time 04 : 40 PM
# Video time 39 : 35 sec

# Date: 27th February 2024 Tuesday
# Start Time 04 : 29 PM

#------------Polymorphism
# Operator Overloading

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(f"{self.real} i + {self.img} j")
    
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
# num1.showNumber()

num2 = Complex(2, 4)
# num2.showNumber()

result = num1 + num2 # It works if you write __add__ instead add
# result = num1.add(num2) # It works if you write add instead __add__
# result.showNumber()

'''
Lets Practice
Qs. Create a class called Order which stores item & its price.
        Use Dunder function _ _ gt __( ) to convey that:
            order1 > order2 if price of order1 > price of order2
'''
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        if self.price > odr2.price:
            return True
        else:
            return False
    
odr1 = Order("chips", 20)
odr2 = Order("tea", 15)
print(odr1 > odr2) # True
# print(odr1.gt(odr2))
#--------------------------------------------------

pairs = [(x, y) for x in range(3) for y in range(2)]
pairs = [(a, b) for a in 'ab' for b in 'ab']
# Output: [('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b')]
# print("Pairs  ", pairs)
list1 = []
for a in "ab":
    # print(a)
    for b in "ab":
        # print(b)
        list1.append((a,b))
# print(list1) # Output: [('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b')]

# Date: 27th February 2024 Tuesday
# End Time 05 : 48 PM