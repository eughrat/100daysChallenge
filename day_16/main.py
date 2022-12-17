# import turtle
#
# timmy = turtle.Turtle()
# tod = turtle.Turtle()
# my_screen = turtle.Screen()
# timmy.shape("turtle")
# timmy.color("red")
# tod.color("blue")
# timmy.forward(100)
# tod.backward(100)
#
#
# print(timmy)
# print(my_screen)
# print(dir(timmy))
# print(dir(my_screen))
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)
