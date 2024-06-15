# Date: 2nd February 2024 Friday
# Start Time : 07 : 24 PM
# Start Coding Time : 07 : 44 PM

class ComplexNumber:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i
    def __add__(self, other):
        # return f"{self.real+other.real} + {self.imaginary+other.imaginary}i"
        return str(self.real+other.real) + "+" + str(self.imaginary+other.imaginary) + "i"

c1 = ComplexNumber(5, 8)
c2 = ComplexNumber(2, 1)
print(c1 + c2)

# Assignment:
# You have to overload the greater than operator
# Just create a class, create two objects of that class person1 and person2 
# with name and age the one who is elder is going to pay the bill
# So you have to compare the age of two persons

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False

p1 = Person("Taimur", 15)
p2 = Person("Awais", 21)
if p1 > p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")
