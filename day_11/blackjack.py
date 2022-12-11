import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_deck = []
computer_deck = []

def pick_a_card(deck):
    card = random.choice(cards)
    deck.append(card)
    return deck

def check_deck(deck):
    if sum(deck) <= 21:
        return True
    elif 11 in deck and sum(deck) > 21:
        idx = deck.index(11)
        deck[idx] = 1
        if sum(deck) == 21:
            return True
    else:
        return False

def game_status(player_deck, computer_deck):
    print(f"Your cards: {player_deck}, current score: {sum(player_deck)}")
    print(f"Computer's first card: {computer_deck[0]}")





while True:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    player_deck = pick_a_card(player_deck)
    player_deck = pick_a_card(player_deck)
    computer_deck = pick_a_card(computer_deck)
    computer_deck = pick_a_card(computer_deck)
    print(logo)
    game_status(player_deck, computer_deck)
    draw_a_card = 'y'
    while play == "y":
        draw_a_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw_a_card == "y":
            player_deck = pick_a_card(player_deck)
            check_player = check_deck(player_deck)
            game_status(player_deck,computer_deck)
            if check_player == False:
                print("You went over. You lose 😭")



















#
# while True:
#     play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#     if play == "n":
#         break
#     while play == "y":
#         player_deck = pick_a_card(player_deck)
#         player_deck = pick_a_card(player_deck)
#         computer_deck = pick_a_card(computer_deck)
#         computer_deck = pick_a_card(computer_deck)
#         print(logo)
#         print(f"Your cards: {player_deck}, current score: {sum(player_deck)}")
#         print(f"Computer's first card: {computer_deck[0]}")
#         draw_a_card = input("Type 'y' to get another card, type 'n' to pass: ")
#         while draw_a_card == 'y':
#             player_deck = pick_a_card(player_deck)
#             print(f"Your cards: {player_deck}, current score: {sum(player_deck)}")
#             print(f"Computer's first card: {computer_deck[0]}")
#             if sum(player_deck) > 21:
#                 print(f"Your final hand: {player_deck}, final score: {sum(player_deck)}")
#                 print(f"Computer's final hand: {computer_deck}, final score: {sum(computer_deck)}")
#                 print("You went over. You lose 😤")
#                 break
#             draw_a_card = input("Type 'y' to get another card, type 'n' to pass: ")
#         if draw_a_card == 'n':
#             while sum(computer_deck) <=21:
#                 computer_deck = pick_a_card(computer_deck)
#                 if sum(computer_deck) > 21:
#                     computer_deck.pop()
#             print(f"Your final hand: {player_deck}, final score: {sum(player_deck)}")
#             print(f"Computer's final hand: {computer_deck}, final score: {sum(computer_deck)}")
#
#         if sum(player_deck) < sum(computer_deck):
#             print("You lose 😤")
#         elif sum(player_deck) > sum(computer_deck):
#             print("You win!")
#         else:
#             print("Draw")
#


















# while play == "y":
#     player_deck = pick_a_card(player_deck)
#     player_deck = pick_a_card(player_deck)
#     while sum(player_deck) <=21:
#         print(logo)
#         print(f"Your cards: {player_deck}, current score: {sum(player_deck)}")
#         computer_deck = pick_a_card(computer_deck)
#         computer_deck = pick_a_card(computer_deck)
#         print(f"Computer's first card: {computer_deck[0]}")
#         draw_a_card = input("Type 'y' to get another card, type 'n' to pass: ")
#         if draw_a_card == "y":
#             player_deck = pick_a_card(player_deck)
#             player_win = check_player(player_deck)
#             if check_player == True:
#                 while sum(computer_deck) <= 21:
#                     computer_deck = pick_a_card(computer_deck)
#                     computer_win = check_player(computer_deck)



