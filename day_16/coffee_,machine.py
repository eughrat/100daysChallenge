import coffee_maker, menu, money_machine
menu = menu.Menu()
coffee_maker =  coffee_maker.CoffeeMaker()
money = money_machine.MoneyMachine()
power = True

while power:
    drink = input(f"What would you like? ({menu.get_items()}): ")
    if drink == "report":
        coffee_maker.report()
        money.report()
    elif drink == "espresso" or drink == "latte" or drink == "cappuccino":
        cost = menu.find_drink(drink).cost
        coffee = menu.find_drink(drink)
        # print(coffee)
        can_make = coffee_maker.is_resource_sufficient(coffee)
        if can_make == False:
            continue
        else:
            is_payment_valid = money.make_payment(cost)
            if is_payment_valid == False:
                continue
            else:
                coffee_maker.make_coffee(coffee)
    elif drink == "off":
        power = False






