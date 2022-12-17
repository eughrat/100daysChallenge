state_of_the_machine = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}

coffee = {
    "espresso": {
        "Water": 50,
        "Milk": 0,
        "Coffee": 18,
        "Money": 1.50
    },
    "latte": {
        "Water": 200,
        "Milk": 150,
        "Coffee": 24,
        "Money": 2.50
    },
    "cappuccino": {
        "Water": 250,
        "Milk": 100,
        "Coffee": 24,
        "Money": 3.00
    }}


def report(state_of_the_machine):
    print(f"Water: {state_of_the_machine['Water']}")
    print(f"Milk: {state_of_the_machine['Milk']}")
    print(f"Coffee: {state_of_the_machine['Coffee']}")
    print(f"Money: {state_of_the_machine['Money']}")


def check_resources(state_of_the_machine, coffee, what_to_do):
    for i in state_of_the_machine:
        if state_of_the_machine[i] == "Money":
            pass
        elif state_of_the_machine[i] < coffee[what_to_do][i]:
            print(f"Sorry there is not enough {i.lower()}.")
            return False
        else:
            return True


def do_a_coffee(what_to_do, state_of_the_machine, money, coffee):
    for i in state_of_the_machine:
        state_of_the_machine[i] = state_of_the_machine[i] - coffee[what_to_do].get(i)
    if money > coffee[what_to_do]["Money"]:
        change = round(money - coffee[what_to_do]["Money"],2)
        print(f"Here is ${change} in change.")
    print(f"Here is your {what_to_do}. Enjoy!")

    return state_of_the_machine

def calculate_coins():
    quarter = int(input("how many quarters?: "))
    dime = int(input("how many dimes?: "))
    nickel = int(input("how many nickels?: "))
    penny = int(input("how many pennies?: "))
    return penny * 0.01 + dime * 0.010 + nickel * 0.05 + quarter * 0.25

power = True

while power:
    what_to_do = input("What would you like? (espresso/latte/cappuccino): ")
    if what_to_do == "report":
        report(state_of_the_machine)
    elif what_to_do == "espresso" or what_to_do == "latte" or what_to_do == "cappuccino":
        money = calculate_coins()
        if money < coffee[what_to_do]["Money"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            check = check_resources(state_of_the_machine, coffee, what_to_do)
            if check == True:
                do_a_coffee(what_to_do,state_of_the_machine, money, coffee)
            else:
                continue
    elif what_to_do == "off":
        break