# Date: 27th January 2024 Saturday
# Time: 04 : 33 PM

# Date: 29th January 2024 Monday
# Time: 03 : 57 PM
# -----------------Start Time: 05 : 42 PM---------------
# -------------------End Time: 08 : 56 PM-----------------
# -----------------------End Time: 09 : 15 PM---------- After writing end wali statements

# Now I am shutting down the computer.I am going to start preparing tomorrow Phase 8 English and Urdu Tests on 30th January 2024
# End Time is 09 : 17 PM  ----29th January 2024

# The four pillars of OOP are:
# 1. Inheritance
# 2. Abstraction
# 3. Encapsulation
# 4. Polymorphism

# We can access private methods and attributes outside of the class.
# There are basically three methods:
# 1. Just create public method within the class only, using that we can access private methods and attributes.
# 2. Using Name Mangling
# 3. Using getter and setter methods

# First two techniques we discussed in previous video

class Student:
    def __init__(self, name, city, age):
        self.name = name  # public object variable
        self._city = city  # protected object variable
        self.__age = age  # private object variable

    def get_age(self): # We use getters and setters on private attributes only
        return self.__age
    def set_age(self, age):
        if age > 30 :
            print("Age is not less than 30")
        else:
            self.__age = age
            
    
#     def __display(self): # Private Method
#         print(f"Hi I am {self.name}. I live in {self._city}. My age is {self.__age}")
#     def display_private_data(self): # Public Method
#         self.__display()

# class Branch(Student):
#     def show(self):
#         print(f"My name is {self.name}")

s1 = Student("Tamoor Akhter Sandhu", "Gaggoo Mandi", 15)
print(s1.get_age())
s1.set_age(22)
print(s1.get_age())

# Means we are hiding something from outside of class. This is Encapsulation.

# Meray kehan da matlab wa ky aapa private attributa nu 2 public method 
# yani aik method dy shuru ch get lga lo ty dosry dy shuru ch set lga lo.
# jidda get_age ty set_age mein banyay
# is tarha bandy nu samaj oundi ky apa age nu change krna cha ry waan.

# Yani Aapa badlan da sara kam class yani Capsule dy under e hal kr lya wa. 
# Yani Class dy bahr badlan dy kam nahi kita. Class di Boundary dy under reh ky kam kita
