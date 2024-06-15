# 31st Oct 2023 Tuesday
# After complete. Time : 09 : 35 PM

size = input("What size pizza you want to order(S\M\L)?")
bill = 0

if size=="S" or size=="s":
    bill += 100
    print("Small pizza price is 100 Rs.")
elif size=="M" or size=="m":
    bill += 200
    print("Medium pizza price is 200 Rs.")
else:
    bill += 300  
    print("Large pizza price is 300 Rs.")

add_pepsi = input("Do you want pepsi (Y/N)?")
if add_pepsi=="y" or add_pepsi=="Y":
    if size=="S" or size=="s":
        bill +=30
    else:
        bill +=50

extra_cheese = input("Do you want pepsi (Y/N)?")
if extra_cheese=="y" or extra_cheese=="Y":
        bill +=20
print(f"Your final bill is {bill}")