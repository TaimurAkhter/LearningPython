# Date: 15th February 2024 Thursday
# Start Time : 07 : 36 PM

# ---------Date: 17th February 2024 Saturday
# ----------Start Time : 01 : 27 PM
# Time : 01 : 57 PM ----------
# End Time : 02 : 10 PM

# Higher Order function is either is a function which either accept a function as an argument or returns a function.

def add(x,y):
    print(f"{x} + {y} = {x+y}")
def subtract(x,y):
    print(f"{x} - {y} = {x-y}") 

# add_sub is a Higher Order Function because it is accepting functions as an argument
def add_sub(new_function, x,y):
    print("Hi")
    new_function(x, y)
    
# add_sub(add, 245,6)
# add_sub(subtract, 212,7)

# calculator is a Higher Order Function because it is returning a function.
def calculator(number):
    print(f"You entered {number}")
    def add(x,y):
        print(f"Result: {x} + {y} = {x+y}")
    def subtract(x,y):
        print(f"Result: {x} - {y} = {x-y}") 
    
    if number==1:
        return add
    else:
        return subtract

# new_func = calculator(1)
# new_func(16, 16)

# Assignment
# Means this is an example of passing a function as an argument
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

def calculate(function, n1, n2):
    if function==add:
        return add(n1,n2)
    if function==sub:
        return sub(n1,n2)
    if function==mul:
        return mul(n1,n2)
    if function==div:
        return div(n1,n2)

new_func = calculate(add, 6, 3)
print(new_func)

# print(type(id(new_func))) # <class 'int'>
# print(0.1 + 0.2 == 0.3) # What it gives: True or False
# print(~4)

# print(0x8d9)
print(complex(3, 1))

