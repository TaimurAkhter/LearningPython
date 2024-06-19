# Date: 6th January 2024 Saturday
# Start Time: 01 : 04 AM
# End Time: 01 : 22 AM
#---------------------Project 6 Tricky Calculator
#-------------------------Jenny Solution--------------------

import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations_dict = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}
#-------------------this is the code of jenny
def calculator():
    number1 = float(input("Enter first number:"))
    for symbol in operations_dict:
        print(symbol) 

    continue_flag = True
    while continue_flag:
        op_symbol = input("Pick an operation:")
        number2 = float(input("Enter next number:"))
        calculator_function = operations_dict[op_symbol]
        output = calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {output}")

        should_continue =  input(f"Enter 'y' to continue calculation with {output} or 'n' to start new calculation or 'x' to exit: ")
        if should_continue == 'y':
            number1 = output
        elif should_continue == 'n':
            continue_flag = False
            os.system('cls')
            calculator() # She use recursion
        else:
            continue_flag = False
            print("Bye")
calculator()