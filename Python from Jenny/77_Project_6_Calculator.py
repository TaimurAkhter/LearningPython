# Date: 5th January 2024 Friday
# Start Time: 11 : 56 PM

# Date: 6th January 2024 Saturday
# End Time: 01 : 01 AM
#---------------------Project 6 Tricky Calculator
import os
def calculator(a, b, operator):
    if operator == "+":
        c = a + b
        return c
    elif operator == "-":
        c = a - b
        return c
    elif operator == "*":
        c = a * b
        return c
    elif operator == "/":
        c = a / b
        return c

again = True
n1 = True
while again:
    if n1 == True:
        num1 = float(input("Enter first number:")) #7
        print("+\n-\n*\n/")
    operation = input("Pick an operation:") #+
    num2 = float(input("Enter next number:")) #1
    
    result = calculator(num1, num2, operation)
    print(f"{num1} {operation} {num2} = {result}")

    should_continue = input(f"Enter 'y' to continue calculation with {result} or 'n' to start new calculation or 'x' to exit: ")
    if should_continue == 'y':
        num1 = result
        n1 = False
    elif should_continue == 'n':
        n1 = True
        os.system('cls')
    else:
        again = False
        print("Bye")