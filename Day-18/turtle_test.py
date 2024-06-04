import turtle as t
from turtle import Turtle, Screen
import random

bruh = Turtle()
bruh.shape('turtle')
bruh.color('DarkBlue')
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

#Dashed Line
""" for _ in range(15):
    bruh.forward(10)
    bruh.penup()
    bruh.forward(10)
    bruh.pendown() """


#Shapes
bruh.speed(200000)
for i in range (3, 100):
    bruh.color(random_color())
    for j in range (i):
        bruh.forward(100)
        bruh.right(360/i)

#Random Walk
""" directions = [0, 90, 180, 270]
bruh.pensize(10)
bruh.speed(200)

for i in range(1, 1001):
    bruh.right(random.choice(directions))
    bruh.color(random_color())
    bruh.forward(100) """


#Spirograph 1
""" bruh.speed(200)
for i in range(1, 361):
    bruh.color(random_color())
    bruh.circle(100)
    bruh.right(1) """

#Spirograph 2
""" bruh.speed(2000)

def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        bruh.color(random_color())
        bruh.circle(100)
        bruh.setheading(bruh.heading() + gap_size)

draw_spirograph(10)


"""
screen = Screen()
screen.exitonclick()
