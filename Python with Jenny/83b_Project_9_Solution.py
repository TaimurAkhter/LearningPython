# Date: 13th January 2024 Friday
# Time: 09 : 06 PM

Menu = {
    "latte": {
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 150
    },
    "espresso": {
        "ingredients":{
            "water": 50,
            "milk": 18,
            "coffee": 0
        },
        "cost": 100
    },
    "cappuccino": {
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 200
    }
}
profit = 0
resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100
}


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
            
def process_coins():
    print("Please inert coins")
    total = 0
    coins_five = int(input("Ho many 5rs coin?: "))
    coins_ten= int(input("Ho many 10rs coin?: "))
    coins_twenty = int(input("Ho many 20rs coin?: "))
    total = coins_five*5 + coins_ten*10 + coins_twenty*20
    return total

def is_payment_successful(money_received,coffee_cost):
    if money_received >= coffee_cost:
        global profit
        profit += coffee_cost
        change = money_received - coffee_cost
        print(f"Here is your Rs.{change} in change.")
        return True
    else:
        print("Sorry That's not enough money.Money refunded")
        return False
        
def make_coffee(coffee_name, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_name}")

is_on = True
while is_on:
    choice = input("What would you like to have? (espresso/latte/cappuccino)")
    if choice=="off":
        is_on = False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs.{profit}")
    else:
        coffee_type = Menu[choice]
        if check_resources(coffee_type['ingredients']):
            payment = process_coins()
            if is_payment_successful(payment, coffee_type['cost']):
                make_coffee(choice, coffee_type['ingredients'])

