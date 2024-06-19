# Date: 22nd January 2024 Monday
# Time: 05 : 49 PM
# Start Time: 08 : 51 PM

# Date: 23rd January 2024 Tuesday
# End Time: 06 : 55 PM
class A:
    def display(self):
        print("display from A class")
class B(A):
    pass
    # def display(self):
    #     print("display from B class")
class C(A):
    def show(self):
        print("Hi from C class")
    pass
    # def display(self):
    #     print("display from C class")
        
class D(B,C):
    pass
    # def display(self):
    #     print("display from D class")

d1 = D()
d1.display()
# print(D.mro())
print(D.__mro__)

# C3 linearization

'''

(F, G, H) in Z class is known as local precedence order
class Z(F, G, H)

F then G then H. This is local precedence order.

The technique to find mro that should follow this local precedence order (F, G, H)

This mro() use C3 linearization algorithm to get mro
'''