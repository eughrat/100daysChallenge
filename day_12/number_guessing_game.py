import random
from art import logo


def number_to_guess():
    return random.randint(1,100)

number = number_to_guess()

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {number}")
diff_lvl = input("Choose a difficulty. Type 'easy' or 'hard': ")

if diff_lvl == "hard":
    no_of_tries = 5
else:
    no_of_tries = 10

print(f"You have {no_of_tries} attempts remaining to guess the number.")

while no_of_tries != 0:
    no_of_tries -= 1
    guess = int(input("Make a guess: "))
    if guess < number:
        print("Too low!")
        print("Guess again.")
    elif guess > number:
        print("Too high!")
        print("Guess again.")
    elif guess == number:
        print(f"You got it! The answer was {guess}.")
        break
    if no_of_tries == 0:
        print("You've run out of guesses, you lose.")
        break









