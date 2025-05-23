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
}

def make_a_coffee(option):
    for ingredientes in option["ingredients"]:
        if option["ingredients"][ingredientes] > resources[ingredientes]:
            return False
    return True


money_in_machine = 0
machine_stop = False
while not machine_stop:
    option = {}
    machine_option = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if machine_option == "off":
        machine_stop = True

    elif machine_option == "report":
        for stock in resources:
            print(f"{stock}: {resources[stock]}")
        print(f"Money: ${money_in_machine}")
    else:
        option = MENU[machine_option]

        if make_a_coffee(option) == False:
            print("Sorry there is not enough water")
        else:
            print("Please insert coin")

            quarters = int(input("How many quarters?: "))
            quarters = quarters * 0.25

            dimes = int(input("How many dimes?: "))
            dimes = dimes * 0.10

            nickles = int(input("How many nickles?: "))
            nickles = nickles * 0.05

            pennies = int(input("How many pennies?: "))
            pennies = pennies * 0.01

            money = quarters + dimes + nickles + pennies

            print(f"Here is ${money} in change.")

            if money >= option["cost"]:
                print(f"Here is you {machine_option}. Enjoy :)")
                money_in_machine += option["cost"]

            else:
                print("sorry you need more money.. :(")