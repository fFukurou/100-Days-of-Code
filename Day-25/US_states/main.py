#State Guess Project

import turtle
import csv

import pandas as pd
from states import States

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day-25/US_states/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0

data = pd.read_csv("Day-25/US_states/50_states.csv")

correct_guesses = []
states_to_learn = []


game_is_on = True
while game_is_on:
    input = screen.textinput(title=f"{score}/{data.shape[0]} States Correct", prompt="What's another state's name?")
    answer_state = str(input).title()

    if answer_state == "" or answer_state == "Exit":
        game_is_on = False

    for state in data['state']:
        if answer_state == state:
            correct_guesses.append(answer_state)
            score += 1
            x_cor = data[data.state == state]['x'].values[0]
            y_cor = data[data.state == state]['y'].values[0]
            new_state = States(state, x_cor, y_cor )

    if score >= 50:
        game_is_on = False

for state in data["state"]:
    if state not in correct_guesses:
        states_to_learn.append(state)

pd.DataFrame(states_to_learn).to_csv("Day-25/US_states/missing_states.csv")

screen.exitonclick()    