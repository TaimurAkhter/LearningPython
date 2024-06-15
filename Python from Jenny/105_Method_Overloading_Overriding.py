# Date: 2nd February 2024 Friday
# Start Time : 07 : 59 PM
# Start Coding Time : 08 : 0 PM

# By default Python does not support Method Overloading
# What is Method Overloading?
# Method Overloading means we are defining multiple or many methods with same name but different arguments in a same class.

# Method Overloading means defining many methods with same name but different arguments within a same class.

class Demo:
    # def add(self, a, b, c=0):
    #     return a + b + c

    def add(self, *args):
        total = 0
        for i in args:
            total = total + i
        return total
    
d = Demo()
print(d.add(200, 51))
print(d.add(200, 1, 4))
print(d.add(21, 128, 42, 37, 19))

# Date: 5th February 2024 Monday
# Continue Time : 05 : 57 PM

class CD70:
    def speed(self):
        print("CD70 run at speed of 70km/h")
    def capacity(self):
        print("Two Persons")
        
class Prider(CD70):
    def speed(self):
        print("Prider run at speed of 100km/h")
        super().speed()
   
a = Prider()
a.speed()


'''
Method Overloading is compile time polymorphism
Method Overriding is run time time polymorphism

Method Overloading occurs (within a same class) we are having multiple methods with same name but different parameters
Although in python we don't have this kind of thing because python does not support Method Overloading So we have only one method

Method Overriding occurs in two classes. It will occur in inheriting. (that is must)

In Method Overloading method must have same name but different no. of parameters
In Method Overriding methods must have same name and same no. of parameters

Python does not support Method Overloading
You can achieve Method Overloading with the help of default arguments or *args

Python supports Method Overriding
'''

# End Time: 09 : 15 PM