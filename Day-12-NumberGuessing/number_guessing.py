#Number Guessing Project
from art import logo
import os
import random

clear = lambda: os.system('cls')

while True:
    tries = 0
    random_number = random.randint(1, 100)
    attemps = 0

    while True:
        clear()
        print(logo)
        difficulty = input("Choose a difficulty: 'easy', 'medium' or 'hard'\n").lower()
        match difficulty:
            case 'easy':
                tries = 20
                break
            case 'medium':
                tries = 10
                break
            case 'hard':
                tries = 5
                break
            case _:
                print('\nInvalid input, please try again.')

    while True:
        print(f"You have {tries} tries.\n")
        answer = int(input("Guess a number from 1 to 100:  "))
        attemps += 1

        if answer == random_number:
            print(f"\nYou won! You got it in {attemps} tries.")
            break
        elif answer < random_number:
            print(f"\nhe number is GREATER than {answer}\n")
            tries -= 1

        elif answer > random_number:
            print(f"\nThe number is LESSER than {answer}\n")
            tries -= 1

        if tries == 0:
            print("You ran out of tries.")
            break

    while True:
        go_again = input("Would you like to go again? (y/n)\n").lower()
        match go_again:
            case 'y':
                break
            case 'n':
                exit("\nThank you for playing.\n")
            case _:
                print("\nInvalid Input.")

