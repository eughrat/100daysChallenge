import random
from game_data import data
from art import logo, vs
from replit import clear

print(logo)

def select_rivals(data):
    data_idxs = [i for i in range(len(data))]
    first_rival = data[random.choice(data_idxs)]
    data.remove(first_rival)
    second_rival = data[random.choice(data_idxs)]
    return first_rival, second_rival

play = True
points = 0

while play:
    first_rival, second_rival = select_rivals(data)
    print(f"Compare A {first_rival['name']}, a {first_rival['description']}, from {first_rival['country']}")
    print(vs)
    print(f"Compare A {second_rival['name']}, a {second_rival['description']}, from {second_rival['country']}")
    choice = (input("Who has more followers? Type 'A' or 'B': ")).upper()
    if choice == "A" and first_rival["follower_count"] > second_rival["follower_count"]:
        points += 1
        print(f"You're right! Current score: {points}")
        clear()
    elif choice == "B" and first_rival["follower_count"] < second_rival["follower_count"]:
        points += 1
        print(f"You're right! Current score: {points}")
        clear()
    else:
        print(f"Sorry, that's wrong. Final score: {points}")
        clear()
        break