state_of_the_machine = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money":0
}

def report(state_of_the_machine):
    print(f"Water: {state_of_the_machine['Water']}")
    print(f"Milk: {state_of_the_machine['Milk']}")
    print(f"Coffee: {state_of_the_machine['Coffee']}")
    print(f"Money: {state_of_the_machine['Money']}")

def do_a_coffee(coffee_type, state_of_the_machine, money):
    espresso = {
        "Water": 50,
        "Milk": 0,
        "Coffee": 18,
        "Money": 1.50
    }
    latte = {
        "Water": 200,
        "Milk": 150,
        "Coffee": 24,
        "Money": 2.50
    }
    cappuccino = {
        "Water": 250,
        "Milk": 100,
        "Coffee": 24,
        "Money": 3.00
    }

def calculate_coins(penny, dime, nickel, quarter):

    return penny * 0.01 + dime * 0.010 + nickel * 0.05 + quarter * 0.25



while True:
    what_to_do = input("What would you like? (espresso/latte/cappuccino): ")
    if what_to_do == "report":
        report(state_of_the_machine)
    elif what_to_do == "espresso" or what_to_do == "latte" or what_to_do == "cappuccino":

