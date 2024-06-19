# Date: 30th January 2024 Tuesday
# Start Time : 05 : 30 PM

# End Time : 05 : 42 PM
# Time 05 : 47 PM 

# After writing the end paragraphs with the help of ChatGPT End Time : 06 : 06 PM

class Duck:
    def swim(self):
        print("Duck can swim")
    def walk(self):
        print("Duck can walk")
        
class Man:
    def swim(self):
        print("Man can swim")
    def walk(self):
        print("Man can walk")
    def eat(self):
        print("Man can eat")

class Birds:
    def walk(self):
        print("Birds can walk")
    
class Demo:
    def display(self, obj):
        obj.swim()
        obj.walk()
        print("Information displayed")

d = Duck()
m = Man()
b = Birds()
demo = Demo()
demo.display(d)
demo.display(m)
# demo.display(b) # Error


# Certainly! Let's break it down further:

# 1. Duck Typing Principle: 
#                          In Python, the type or class of an object is not explicitly checked; instead, the focus is on whether the object has the required methods or attributes.

# 2. Required Methods: 
#                     In the example, the "display" method of the "Demo" class expects the object passed to it ("obj") to have two methods: "swim()" and "walk()".

# 3. Irrespective of Class: 
#                          The "display" method doesn't care about the actual class of the object ("Duck", "Man", or any other class). It only cares that the object can perform the necessary actions, which are swimming ( "swim()" ) and walking ( "walk()" ).

# So, when we say "as long as an object has the required methods (swim() and walk()), it
# can be passed to the display method, irrespective of its actual class," it means that any
# object with the right capabilities (methods) can be used with the "display" method.

# The class name doesn't matter; what matters is whether the object can perform the
# actions expected by the method. This is the essence of duck typing in Python.
