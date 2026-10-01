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
    "money": 10.0,
}

def show_resources(current_resources):
    """When called, this prints the current amount of resources in a readable format."""
    # For every key and value it'll loop through and display the current resources with the correct measurements.
    for key, value in current_resources.items():
        if key == "water":
            print(f"{key}: {value}ml")
        elif key == "milk":
            print(f"{key}: {value}ml")
        elif key == "coffee":
            print(f"{key}: {value}g")
        elif key == "money":
            print(f"{key}: ${value}")


def process_coins():
    """This asks and receives the amount of coins that the user gives and returns the total."""
    print("Please insert coins.")

    quarters = float(input("How many quarters?: ")) * .25
    dimes = float(input("How many dimes?: ")) * .1
    nickels = float(input("How many nickels?: ")) * .05
    pennies = float(input("How many pennies?: ")) * .01

    total_amount = float(quarters + dimes + nickels + pennies)
    return total_amount

def check_payment(user_paid, order, current_resources):
    """This checks to see if the user has enough money based on the input from the 'process_coins()' function. If it doesn't it will
    return False. If it does, it will return True."""
    if user_paid < MENU[order]["cost"]:
        print("Sorry, that's not enough. Money refunded.")
        return False
    elif user_paid == MENU[order]["cost"]:
        current_resources["money"] += user_paid
    elif user_paid > MENU[order]["cost"]:
        current_resources["money"] += user_paid
        user_change = round(user_paid - MENU[order]["cost"], 2)
        current_resources["money"] -= user_change
        print(f"Here is your change: ${user_change}")
    return True

def check_resources(current_resources, order):
    """This will check if there are enough resources. If there are not enough, it will return False."""

    required_ingredients = MENU[order]["ingredients"]

    for ingredient, amount_needed in required_ingredients.items():
        if current_resources[ingredient] < amount_needed:
            print(f"There is not enough {ingredient}.")
            return False
    return True

def make_coffee(current_resources, order):
    """This will deduct the amount of resources that the coffee needs then give the drink."""
    order = MENU[order]["ingredients"]
    for ingredient, amount_needed in order.items():
        if ingredient in current_resources:
            current_resources[ingredient] -= amount_needed

    print(f"Here is your coffee: ☕")


####################################### Starts here #####################################
machine_running = True
while machine_running:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        machine_running = False
    elif user_choice == "report":
        show_resources(resources)
    elif user_choice in MENU:
        if check_resources(resources, user_choice) == True:
            total_money = process_coins()
            enough_money = check_payment(total_money, user_choice, resources)
            if enough_money == True:
                make_coffee(resources, user_choice)
            else:
                continue
        else:
            continue
    else:
        print("That is an invalid option. Please try again.")