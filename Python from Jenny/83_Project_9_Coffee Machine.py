# Date: 8th January 2024 Saturday ------------ko File Create ki thi
# Time: 07 : 49 AM
# Date: 10th January 2024 Saturday
# Time: 08 : 55 PM
# Date: 11 January 2024 Thursday Kurulus osman wekhi ty chemistry di tyari krda si
# Time: 05 : 03 PM
#---------------------------------------------------------------------------------------
# Date: 12 January 2024 Friday ----------Project 9 Coffee Machine
# Time: 02 : 08 PM
# Start Time: 02 : 18 PM #-****-------lga tar yani 2ghnty kmm krlo
# End Time: 09 : 52 PM

# ---------------------------Date: 13th January 2024 Saturday
# ---------------------------End Time: 11 : 45 PM ----------------COMPLETE FULL

import os
Menu = {
    "espresso": {
        "ingredients":{
            "water": 50,
            "milk": 18
        },
        "cost": 100
    },
    "latte": {
        "ingredients":{
            "water": 200,
            "milk": 50,
            "coffee": 50
        },
        "cost": 150
    },
    "cappuccino": {
        "ingredients":{
            "water": 200,
            "milk": 100,
            "coffee": 50
        },
        "cost": 200
    }
}
profit = 0
resources = {
    "water": 500,
    "milk": 286,
    "coffee": 100
}

def find_name(choice):
    if choice == "espresso":
        return "espresso"
    elif choice == "latte":
        return "latte"
    elif choice == "cappuccino":
        return "cappuccino"
    else:
        return False

def check_ingredients(coffee_ingredient, resources):
    for item in coffee_ingredient:
        if coffee_ingredient[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    global receive_money
    receive_money = int(input("How much money you give: "))
    if coffee['cost'] > receive_money:
        os.system('cls')
        print("Sorry That's not enough money.Money refunded")
        return False
    
    for item in coffee_ingredient:
        resources[item] = resources[item] - coffee_ingredient[item]
    return True

def report():
    print("Resources:")
    print(f"          Water: {resources['water']}ml")
    print(f"          Milk: {resources['milk']}ml")
    print(f"          Coffee: {resources['coffee']}g")
    print(f"          Money: {profit}")

sales = {
    'espresso':0,
    'latte':0,
    'cappuccino':0
}

AGAIN = True
while AGAIN:
    choice = input("What would you like to have? (espresso/latte/cappuccino)")
    name_of_coffee = find_name(choice) # espresso
    if choice == "off":
        AGAIN = False
    elif choice == "report":
        os.system('cls')
        report()
    elif choice == "data":
        os.system('cls')
        report()
        print("Sales:")
        for i in sales:
            print(f"      {i}:{sales[i]}")
    else:
        coffee = Menu[name_of_coffee] # latte
        if check_ingredients(coffee["ingredients"], resources):
            sales[name_of_coffee] += 1
            profit += coffee['cost']
            os.system('cls')
            print(f"Here is your Rs.{receive_money-coffee['cost']} in change.")
            print(f"Here is your {name_of_coffee}")

# report
# latte
# cappuccino
# espresso