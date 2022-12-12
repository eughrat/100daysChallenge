import random
import os
from art import logo


clear = lambda: os.system('cls')

def deal_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)

def game_status(player_deck, computer_deck):
    print(f"    Your cards: {player_deck}, current score: {sum(player_deck)}")
    print(f"    Computer's first card: {computer_deck[0]}")

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "    You went over. You lose 😤"
    if user_score == computer_score:
        return "    Draw 🙃"
    elif computer_score == 0:
        return "    Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "    Win with a Blackjack 😎"
    elif user_score > 21:
        return "    You went over. You lose 😭"
    elif computer_score > 21:
        return "    Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "    You win 😃"
    else:
        return "    You lose 😤"



def final_status(player_deck, computer_deck):
    print(f"    Your final hand: {player_deck}, final score: {sum(player_deck)}")
    print(f"    Computer's final hand: {computer_deck}, final score: {sum(computer_deck)}")

def play_game():
    print(logo)
    player_deck = []
    computer_deck = []


    for i in range(2):
        player_deck.append(deal_a_card())
        computer_deck.append(deal_a_card())

    while True:
        user_score = calculate_score(player_deck)
        computer_score = calculate_score(computer_deck)
        game_status(player_deck, computer_deck)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            final_status(player_deck,computer_deck)
            return user_score, computer_score
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                player_deck.append(deal_a_card())
            else:
                final_status(player_deck,computer_deck)
                return user_score, computer_score

    while computer_score != 0 and computer_score < 17:
        computer_deck.append(deal_a_card())
        computer_score = calculate_score(computer_deck)
        final_status(player_deck,computer_deck)

    return user_score, computer_score

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    user_score, computer_score = play_game()
    print(compare(user_score, computer_score))

