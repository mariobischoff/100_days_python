MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

status = "on"

from os import system

clear = lambda: system("cls")

def report():
    """Print resources that contain on the machine"""
    for i in resources:
        print(f"{i.capitalize()}: {resources[i]}")


def check_resources(flavor):
    """Check if resources is enough"""
    ingredients = MENU[flavor]["ingredients"]
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            return False
    return True


def process_coin(flavor):
    """"""
    peny = int(input("Peny: "))
    nickel = int(input("Nickel: "))
    dime = int(input("Dime: "))
    quarter = int(input("Quarter: "))
    total = peny * 0.01 + nickel * 0.05 + dime * 0.1 + quarter * 0.25
    cost = MENU[flavor]["cost"]
    change = 0
    if cost > total:
        return {"result": False, "message": "Sorry that's not enough money. Money refunded."}
    else:
        change = total - cost
        return {"result": True, "message": f"Here is ${change:.2f} in change.", "profit": cost}


def make_coffee(flavor):
    """Recive a flavor and make a coffee"""
    if check_resources(flavor):
        coins_enough = process_coin(flavor)
        if coins_enough["result"]:
            print(coins_enough["message"])
            ingredients = MENU[flavor]["ingredients"]
            resources["money"] += coins_enough["profit"] 
            for i in ingredients:
                resources[i] -= ingredients[i]
            print("Coffee Done done ✔")
        else:
            print(coins_enough["message"])
    else:
        print("Don't have enough resources")


while status != "off":
    flavor = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if flavor == "off":
        status = "off"
    elif flavor == "report":
        report()
    elif flavor in MENU:
        make_coffee(flavor)
    else:
        clear()
