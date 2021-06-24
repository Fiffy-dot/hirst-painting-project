# import colorgram
#
# # Extract 10 colors from our image.
# colors = colorgram.extract('image.jpg', 10)
#
# color_tuples = []
#
# for color in range(len(colors)):
#     color = colors[color]
#     rgb = color.rgb
#     red = rgb[0]
#     green = rgb[1]
#     blue = rgb[2]
#     tuples = (red, green, blue)
#     color_tuples.append(tuples)
#
#
# print(color_tuples)
import turtle as t
from turtle import Screen
import random

t.colormode(255)
turtle = t.Turtle()

colors_list = [(225, 229, 237), (241, 234, 211), (243, 228, 240), (222, 241, 230), (193, 165, 118), (138, 164, 194),
               (143, 92, 50), (56, 100, 142), (220, 209, 123), (186, 147, 169)]

turtle.hideturtle()
turtle.speed(0)
for rows in range(10):
    place = turtle.pos()
    for dot in range(10):
        turtle.dot(20, random.choice(colors_list))
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.dot(20, random.choice(colors_list))
    turtle.penup()
    turtle.setpos(place)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)

my_screen = Screen()
my_screen.exitonclick()

