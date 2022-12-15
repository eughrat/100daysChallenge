import random
from game_data import data
from art import logo, vs

print(logo)

def select_rivals(data):
    data_idxs = [i for i in range(len(data))]

    first_rival = data[random.choice(data_idxs)]
    second_rival = data[random.randint(0, len(data) - 1)]
    while first_rival == second_rival:
        first_rival = data[random.randint(0, len(data) - 1)]
        second_rival = data[random.randint(0, len(data) - 1)]

    return first_rival, second_rival

print(select_rivals(data))
