MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}

machine_on = True
#TODO Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino)")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(resources)
    else:
        water_needed = MENU[choice]["ingredients"]["water"]
        milk_needed = MENU[choice]["ingredients"]["milk"]
        coffee_needed = MENU[choice]["ingredients"]["coffee"]

        water_resource = resources["water"]
        milk_resource = resources["milk"]
        coffee_resource = resources["coffee"]

        if water_needed > water_resource:
            print("Sorry there is not enough water")

        elif milk_needed > milk_resource:
            print("Sorry there is not enough water")

        elif coffee_needed > coffee_resource:
            print("Sorry there is not enough coffee")

        else:
            print("Insert coin")
            quarter = int(input("how many quarters?"))
            dime = int(input("how many dimes?"))
            nickel = int(input("how many nickels?"))
            penny = int(input("how many penny?"))
            total_insert = quarter*0.25 + dime*0.10 + nickel*0.05 + penny*0.01

            if total_insert < MENU[choice]["cost"]:
                print("Sorry that's not enough money. Money refunded")

            else:
                resources["water"] = water_resource - water_needed
                resources["milk"] = milk_resource - milk_needed
                resources["coffee"] = coffee_resource - coffee_needed
                resources["money"] += MENU[choice]["cost"]
                if total_insert > MENU[choice]["cost"]:
                    change = round(total_insert - MENU[choice]["cost"], 2)
                    print(f"Here is $ {change} in change.")
                print(f"Here's your {choice}. Enjoy your drink!")


#TODO Turn off the Coffee Machine by entering “ off ” to the prompt.

#TODO Print Report

#TODO Check if resources are sufficient

#TODO Process coins. Quarters 0.25, dimes 0.10, nickel 0.05, pennies 0.01

#TODO Check if transaction is successful

#TODO make the drink. Deduct ingredients from the coffee machine resources. Tell user to enjoy the chosen drink