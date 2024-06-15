# Date: 20th Dec 2023 Wednesday
# Time: 10 : 06 AM
# Start Time: 10 : 49 AM

# ----------Arbitrary arguments are of two types----------
#   -------Arbitrary Positional Arguments (*args)------
'''
def add(*numbers, name): # It convert into tuple (1, 3, 5, 7, 15) 
    c = 0
    print(numbers) 
    print(name) 
    for i in numbers:
        c += i
    print(f"Sum is {c}")

add(7, 6, name="Tamoor")
'''
# -------Arbitrary Keyword Arguments (**kwargs)------
#   ------(**kwargs) convert into dictionary------
'''
def info_person(*args, **kwargs):
    for key,value in kwargs.items():
        print(key,value)
    print(args)

info_person(8, 3, name="Taimur", age=15, lang="Python")
info_person(3, 8, name="Mamoon", age=20, lang="C++")
'''

# Date: 20th Dec 2023 Wednesday
# End Time: 11 : 22 AM

def multiply(*num): #(2, 3, -6, 8)
    a = 1
    for i in num:
        a *= i
    print(f"Total is {a}")

multiply(2, 3, -6, 8)
multiply(2, 5, 8, 9, 0, 6)

# End Time: 11 : 37 AM