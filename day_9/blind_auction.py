import os

from art import logo


def get_max_key_value(dict_of_bids):
    max_bid = 0
    name = "key"
    for key in dict_of_bids.keys():
        if dict_of_bids[key] > max_bid:
            max_bid = dict_of_bids[key]
            name = key
        else:
            pass
    return name, max_bid


print(logo)
play = "yes"
dict_of_bids = {}

while play == "yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    dict_of_bids[name] = bid
    play = input("Are there any other bidders? Type 'yes or 'no'.\n")
    os.system('cls')
    if play == "no":
        bidder_name, max_bid = get_max_key_value(dict_of_bids)
        print(f"The winner is {bidder_name} with a bid of ${max_bid}")



