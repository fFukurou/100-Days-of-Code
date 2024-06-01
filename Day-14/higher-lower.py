import os
import random
from art import logo, vs
from game_data import data

clear = lambda: os.system('cls')
clear()

repeated_choices = []
score = 0
print(logo)

a = data[random.randint(0, len(data) - 1)]
repeated_choices.append(a)
while True:
    b = data[random.randint(0, len(data) - 1)]
    if b != a and b not in repeated_choices: break

while True:
    print(f"Compare A: {a['title']}, a {a['year']} game from {a['developer']}")
    print(vs)
    print(f"Against B: {b['title']}, a {b['year']} game from {b['developer']}")
    answer = input("Which has more sales (in Millions)? Type 'A' or 'B':  ").upper()

    if a['sales'] > b['sales']:
        correct_answer = 'A'
        last_choice = a
        wrong_choice = b
    else:

        correct_answer = 'B'
        last_choice = b
        wrong_choice = a

    if last_choice not in repeated_choices: repeated_choices.append(last_choice)
    else: repeated_choices.append(wrong_choice)


    if answer == correct_answer:
        clear()
        print("-- You got it RIGHT! --")
        score += 1
        if len(repeated_choices) >= 50:
            exit(f"You won! You got a perfect {score} score! Impressive.")

        a = last_choice
        while True:
            b = data[random.randint(0, len(data) - 1)]
            if b != a and b not in repeated_choices: break

    else:
        print(f"\nYou got it WRONG.\nFinal Score: {score}.")
        break

