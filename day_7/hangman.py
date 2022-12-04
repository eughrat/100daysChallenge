import random
from hangman_art import stages, logo
from hangman_words import word_list


print(logo)
word = random.choice(word_list)
word = [i for i in word]
floor = ["_" for i in word]
chances = len(stages)
used = set()
position = -1
print(word)


while chances != 0:
    letter = input("Guess a letter: ")
    used.add(letter)
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                floor[i] = letter
        print(" ".join(floor))
        if word == floor:
            print("You win!")
            break
        print(stages[position])
    else:
        chances -= 1
        position -= 1
        print(f"You guessed {letter}, that's not in the word. You lose a life.")
        print(" ".join(floor))
        if chances == 0:
            print("Yoo lose.")
            break
        print(stages[position])



