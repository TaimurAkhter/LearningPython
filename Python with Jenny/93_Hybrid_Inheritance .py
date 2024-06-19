# Create this file on
# Date: 20th January 2024 Saturday
# Time: 11 : 01 PM

# Date: 21th January 2024 Sunday
# Start Time: 02 : 07 PM
# End Time: 02 : 11 PM

class A:
    def display(self):
        print("display from A class")
class B(A):
    def display(self):
        print("display from B class")
class C:
    def show(self):
        print("Hi from C class")
        
class D(B,C):
    def display(self):
        print("display from D class")

d1 = D()
d1.display()
print(D.mro())