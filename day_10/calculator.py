import os

from art import logo


print(logo)
choice = 'y'

def math_operation(first_number, last_number, operator):
    if operator == "+":
        print(f"{first_number} + {last_number} = {first_number + last_number}")
        return first_number + last_number
    elif operator == "-":
        print(f"{first_number} - {last_number} = {first_number - last_number}")
        return first_number - last_number
    elif operator == "*":
        print(f"{first_number} * {last_number} = {first_number * last_number}")
        return first_number * last_number
    elif operator == "/":
        print(f"{first_number} / {last_number} = {first_number / last_number}")
        return first_number / last_number

initial_number = float(input("What's the first number?: "))


while choice == 'y':

    print(f"+\n-\n*\n/")
    operation = str(input("Pick an operation: "))
    next_number = float(input("What's the next number?: "))
    result = math_operation(initial_number,next_number,operation)
    initial_number = result
    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if choice == "n":
        os.system('cls')
        print(logo)
        initial_number = float(input("What's the first number?: "))
        choice = "y"
