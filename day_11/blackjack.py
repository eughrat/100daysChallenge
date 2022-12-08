import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_deck = []
computer_deck = []

def pick_a_card(deck):
    card = random.choice(cards)
    deck.append(card)
    return deck

def check_if_win(deck):
    if sum(deck) == 21:
        return True
    elif 11 in deck and sum(deck) > 21:
        idx = deck.index(11)
        deck[idx] = 1
        if sum(deck) == 21:
            return True
    else:
        return False



play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while play == "y":
    player_deck = pick_a_card(player_deck)
    player_deck = pick_a_card(player_deck)
    while sum(player_deck) <=21:
        print(logo)
        print(f"Your cards: {player_deck}, current score: {sum(player_deck)}")
        computer_deck = pick_a_card(computer_deck)
        computer_deck = pick_a_card(computer_deck)
        print(f"Computer's first card: {computer_deck[0]}")
        draw_a_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw_a_card == "y":
            player_deck = pick_a_card(player_deck)
            player_win = check_if_win(player_deck)


