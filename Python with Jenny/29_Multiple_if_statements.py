# 31st Oct 2023 Tuesday
# Time : 07 : 36 PM

height = float(input("What is your height?"))
ticket = 0
if height>=3:
    print("You can ride")
    age = int(input("What is your age?"))

    if age < 12:
        ticket = 150
        print(f"Ticket Price is 150 Rs.")
    elif age <= 18:
        ticket = 250
        print(f"Ticket Price is 250 Rs.")
    else:
        ticket = 500
        print(f"Ticket Price is 500 Rs.")

    pic = input("You want to take photo (Y/N)?")
    if pic=="y" or pic=="Y":
        ticket += 50
    print(f"Your total bill is {ticket} Rs.")
else:
    print("You cannot ride")
print("bye")