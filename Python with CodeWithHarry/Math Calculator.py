# variables

input1 = int(input("Enter 1st Number : "))
input2 = int(input("Enter 2nd Number : "))

inputTell = input("Choose your operator (+,-,*,/,//,**,MOD) : ")
inputTell6 = input("Choose your operator: ")

# if inputTell == "+":
#     print(input1 + input2)

# elif inputTell == "-":
#     print(input1 - input2)

# elif inputTell == "*":
#     print(input1 * input2)

# elif inputTell == "/":
#     print(input1 / input2)

# elif inputTell == "**":
#     print(input1 ** input2)

# elif inputTell == "MOD":
#     print(input1 % input2)

# elif inputTell == "//":
#     print(input1 // input2)
# else : 
#     print("Invaild Operator Error!")

match inputTell:
    case "+":
        print(input1 + input2)
    case "-":
        print(input1 - input2)
    case "*":
        print(input1 * input2)
    case "/":
        print(input1 / input2)
    case "//":
        print(input1 // input2)
    case "**":
        print(input1 ** input2)
    case "MOD":
        print(input1 % input2)
    case _:
        print("Invaild Operator Error!")