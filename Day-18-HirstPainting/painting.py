#Hirst Painting Project
import colorgram
import turtle as t
from turtle import Screen
import random

#Extracts colors from an image
""" 
rgb_colors = []
colors = colorgram.extract('Day-18-HirstPainting/image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r ,g, b)
    rgb_colors.append(new_color)

print(rgb_colors) """

screen = Screen()
screen.bgcolor('black')

t.colormode(255)
bruh = t.Turtle()
bruh.speed(2000)
bruh.hideturtle()
bruh.penup()

color_list = [(1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), 
          (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), 
          (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), 
          (229, 173, 165)]

bruh.setheading(225)
bruh.forward(300)
bruh.setheading(0)

number_of_dots = 100
dots_per_line = 10
spacing = 50

for dot_count in range(1, number_of_dots + 1):
    bruh.pendown()
    bruh.dot(20, random.choice(color_list))
    bruh.penup()
    bruh.forward(spacing)

    if dot_count % dots_per_line == 0:
        bruh.setheading(90)
        bruh.forward(spacing)
        bruh.setheading(180)
        bruh.forward(spacing * dots_per_line)
        bruh.setheading(0)




screen.exitonclick()