from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red", "green")
timmy_the_turtle.dot()

def turtle_color():
    r = random.random()
    g = random.random()
    b = random.random()
    tup = (r, g, b)
    return tup

# DRAW A SQUARE

# for _ in range(4):
#     for i in range(20):
#         timmy_the_turtle.penup()
#         timmy_the_turtle.forward(5)
#         timmy_the_turtle.pendown()
#         timmy_the_turtle.forward(5)
#     timmy_the_turtle.left(90)


# DRAW A POLYGON WITH AN INCREASING NUMBER OF SIDE

# nr_of_sides = [3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in nr_of_sides:
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     tup = (r, g, b)
#     timmy_the_turtle.pencolor(tup)
#     for j in range(1, i + 1):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.left((360 / i))


# RANDOM WALK

turns = [0, 90, 180, 270]

for _ in range(100):
    r = random.random()
    g = random.random()
    b = random.random()
    tup = (r, g, b)
    print(tup)
    timmy_the_turtle.pencolor(tup)
    angle = random.choice(turns)
    timmy_the_turtle.forward(50)
    timmy_the_turtle.left(angle)


# DRAW A SPIROGRAPH

# timmy_the_turtle.speed(10)
#
# # for i in range(1,90):
#     color = turtle_color()
#     timmy_the_turtle.pencolor(color)
#     timmy_the_turtle.circle(100)
#     timmy_the_turtle.left(4)


screen = Screen()
screen.exitonclick()
