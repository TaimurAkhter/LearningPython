# Date: 6th January 2024 Saturday
# Start Time: 09 : 45 PM
# End Time: 10 : 08 PM

# 1. If you want to modify a global variable from inside a function then you can use (global) keyword
# a = 10 # global
def display():
    a = 20
    def show():
        global a # 2. global keyword is used to create a global variable from inside function
        a = 30
    print(f"value of a before calling show() function is {a}")
    show()
    print(f"value of a after calling show() function is {a}")

display()
print(a)

name = "Tamoor"
def display():
    global name
    name = name + " Akhter"
print(name)
display()
print(name)