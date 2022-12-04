import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = "! # $ % & ( _ 8 +".split(" ")
numbers = "0 1 2 3 4 5 6 7 8 9".split(" ")

num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like in your password?\n"))
num_of_numbers = int(input("How many numbers would you like in your password?\n"))

l = []
s = []
n = []

for i in range(num_of_letters):
    l.append(letters[random.randint(0,len(letters)-1)])
for i in range(num_of_symbols):
    l.append(symbols[random.randint(0,len(symbols)-1)])
for i in range(num_of_numbers):
    l.append(numbers[random.randint(0,len(numbers)-1)])

output = l+s+n
random.shuffle(output)
print("".join(output))