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
    check = []
    for i in state_of_the_machine:
        if state_of_the_machine.get(i) >= coffee[what_to_do].get(i):
            check.append(True)
    if any(check) == False:
        return False
    else:
        return True


def do_a_coffee(what_to_do, state_of_the_machine, money, coffee):


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
            check = check_resources()
            if check == True:
                do_a_coffee()
            else:
                print("Sorry there is not enough water.")
