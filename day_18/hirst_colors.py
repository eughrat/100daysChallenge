from turtle import Turtle
import colorgram
import random

colors = colorgram.extract('hirst.jpg', 6)
colors_rgb = [(i.rgb.r / 255, i.rgb.g / 255, i.rgb.b / 255) for i in colors]

timmy = Turtle()
timmy.penup()
position = -250
timmy.setposition(-250,position)
for i in range(10):
    for j in range(10):
        timmy.forward(50)
        timmy.dot(20, random.choice(colors_rgb))
    position += 50
    timmy.setposition(-250, position)





