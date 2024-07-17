#Etch a Sketch Project

import dis
from turtle import Turtle, Screen

bruh = Turtle()
bruh.pencolor('white')
screen = Screen()
screen.bgcolor('black')

def move_forwards():
    bruh.forward(10)

def turn_right():
    bruh.right(10)

def turn_left():
    bruh.left(10)

def move_backwards():
    bruh.backward(10)

def clear():
    bruh.penup()
    bruh.clear()
    bruh.home()
    bruh.pendown()

screen.listen()
screen.onkeypress(key='w', fun = move_forwards)   
screen.onkeypress(key='a', fun = turn_left)   
screen.onkeypress(key='s', fun = move_backwards)   
screen.onkeypress(key='d', fun = turn_right)   
screen.onkeypress(key='c', fun = clear)   
screen.exitonclick()

