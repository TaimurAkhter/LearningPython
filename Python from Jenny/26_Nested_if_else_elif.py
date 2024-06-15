# 31st Oct 2023 Tuesday
# Time : 01 : 47 PM

height = int(input("What is your height:"))

if height >= 3:
    print("You can ride")
    age = int(input("Enter your age:"))
    if age < 12:
        print("Pay Rs. 150")
    if age <=18:
        print("Pay Rs. 250")
    else:
        print("Pay Rs. 500")
else:
    print("You cannot ride")
print("Learning Python")