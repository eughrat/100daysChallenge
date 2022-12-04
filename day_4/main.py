# import random
# import my_module
#
# c = random.randint(1,20)
# d = random_float = random.random()
# print(d)
# print(c)
# print(my_module.pi)

import random


# coin_toss = random.randint(0,1)
# print(coin_toss)
# if coin_toss == 0:
#     print("Heads")
# else:
#     print("Tails")

# 🚨 Don't change the code below 👇
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
position = str(position)
column = int(position[0])-1
row = int(position[1])

if row == 1:
    row1[column] = "X"
elif row == 2:
    row2[column] = "X"
else:
    row3[column] = "X"




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")