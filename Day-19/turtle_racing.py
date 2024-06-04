import dis
import random
from turtle import Turtle, Screen

is_race_on = False
starting_y_position = 100
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

screen = Screen() 
screen.bgcolor('black')
screen.setup(width=500, height=400)
while True: 
    user_bet = screen.textinput(title="Make your bet", prompt= "Which turtle will win the race? Type a color (red/orange/yellow/green/blue/purple):  ")
    if user_bet == 'red' or user_bet == 'orange' or user_bet == 'yellow' or user_bet == 'green' or user_bet == 'blue' or user_bet == 'purple': break

for turtle_index in range(0, 6):
    turtle = Turtle("turtle")
    turtle.color(colors[turtle_index])
    turtle.write("The race is on!",font=("Arial",15,"normal"))
    turtle.penup()
    turtle.goto(x=-230, y=starting_y_position)
    turtle.speed(random.randint(1 , 10))
    turtles.append(turtle)
    starting_y_position -= 35

if user_bet:
    is_race_on = True

for turtle in turtles:
    turtle.clear()

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() >= 230:
            winning_turtle = turtle.pencolor()
            is_race_on = False

            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
                turtle.goto(0, 0)
                turtle.write(f"You've won! The {winning_turtle} turtle is the winner!",font=("Arial",10,"normal"))
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")
                turtle.goto(0, 0)
                turtle.write(f"You've lost! The {winning_turtle} turtle is the winner!",font=("Arial",10,"normal"))


screen.exitonclick()