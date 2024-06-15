# 31st Oct 2023 Tuesday
# Time : 08 : 50 PM

print("1. Small Pizza = Rs.100\n2. Medium Pizza = Rs.200\n3. Large Pizza = Rs.300")
user_input = int(input("(0 to exit)\nWhat size pizza you want to order(1,2,3)?"))
bill = 0

if user_input==1:
    bill = 100
    want_Pepsi = input("You want to add pepsi of 50 Rs. (Y/N)?")
    extra_Cheese = input("You want to add Extra Cheese  of 20 Rs. (Y/N)?")
    if want_Pepsi=="y" or want_Pepsi=="Y":
        bill += 50
    if extra_Cheese=="y" or extra_Cheese=="Y":
        bill += 20    
    print(f"Your final bill is {bill}")

elif user_input==2:
    bill = 200
    want_Pepsi = input("You want to add pepsi of 100 Rs. (Y/N)?")
    extra_Cheese = input("You want to add Extra Cheese  of 20 Rs. (Y/N)?")
    if want_Pepsi=="y" or want_Pepsi=="Y":
        bill += 100
    if extra_Cheese=="y" or extra_Cheese=="Y":
        bill += 20    
    print(f"Your final bill is {bill}")

elif user_input==3:
    bill = 300
    want_Pepsi = input("You want to add pepsi of 100 Rs. (Y/N)?")
    extra_Cheese = input("You want to add Extra Cheese  of 20 Rs. (Y/N)?")
    if want_Pepsi=="y" or want_Pepsi=="Y":
        bill += 100
    if extra_Cheese=="y" or extra_Cheese=="Y":
        bill += 20    
    print(f"Your final bill is {bill}")

else:
    print("You do no want to buy.")

print("Exercise 9 Completed!!!")



# 31st Oct 2023 Tuesday
# After Modifying Time : 09 : 43 PM
'''
user_input = int(input("What size pizza you want to order(1,2,3)?"))
bill = 0

if user_input==1:
    bill = 100 
    print("Small pizza price is 100 Rs.")
elif user_input==2:
    bill = 200
    print("Medium pizza price is 200 Rs.")
else:
    bill = 300
    print("Large pizza price is Rs.")

want_Pepsi = input("You want to add pepsi of 100 Rs. (Y/N)?")
if want_Pepsi =="Y" or want_Pepsi =="y":
    if user_input==1:
        bill +=50
else:
    bill +=100

extra_Cheese = input("You want to add Extra Cheese  of 20 Rs. (Y/N)?")
if extra_Cheese =="Y" or extra_Cheese =="y":
        bill +=20
print(f"Your final bill is {bill}")
'''