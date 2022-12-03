print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
how_many_people = int(input("How many people to split the bill? "))

payment_per_person = (total_bill + total_bill * tip/100) / how_many_people

print(f"Each person should pay ${round(payment_per_person, 2)}")


