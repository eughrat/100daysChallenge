import random


rock = '''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_move = int(input("Rock (1), paper (2) or scissors (3)?"))

if player_move == 1:
    print(rock)
elif player_move == 2:
    print(paper)
elif player_move == 3:
    print(scissors)
else:
    print("Incorrect move, you lose!")

computer_move = random.randint(1,3)
if player_move == 1:
    print(rock)
elif player_move == 2:
    print(paper)
elif player_move == 3:
    print(scissors)

if computer_move == player_move:
    print("It's a tie!")
elif computer_move == 1 and player_move == 2:
    print("You won!")
elif computer_move == 2 and player_move == 1:
    print("Computer won!")
elif computer_move == 2 and player_move == 3:
    print("You won!")
elif computer_move == 3 and player_move == 2:
    print("Computer won!")
elif computer_move == 3 and player_move == 1:
    print("You won!")
elif computer_move == 3 and player_move == 1:
    print("Computer won!")


