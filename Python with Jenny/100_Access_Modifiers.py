# Date: 29th January 2024 Monday
# Start Time: 03 : 57 PM
# End Time: 04 : 50 PM

# 24th Oct 2023 to 29th Jan 2024 --------------98 DAYs Hogaye

class Student:
    def __init__(self, name, city, age):
        self.name = name  # public object variable
        self._city = city  # protected object variable
        self.__age = age  # private object variable

    def __display(self): # Private Method
        print(f"Hi I am {self.name}. I live in {self._city}. My age is {self.__age}")
    def display_private_data(self): # Public Method
        self.__display()

class Branch(Student):
    def show(self):
        print(f"My name is {self.name}")   

# b1 = Branch("Tamoor Akhter Sandhu", "Gaggoo Mandi", 15)
# print(b1.name)
# print(b1._city)
# b1.show()
# print(b1.__age) # Error
# b1.__display() # Error

s1 = Student("Tamoor Akhter Sandhu", "Gaggoo Mandi", 15)
s1.display_private_data()

# The way of accessing private methods and attributes using -----Name Mangling Method---
# print(dir(Student)) # It gives list like '_Student__display' etc.

# First underscore (_) then class name (Student) then (_ _) then private method or attribute name
s1._Student__display()
print(s1._Student__age)