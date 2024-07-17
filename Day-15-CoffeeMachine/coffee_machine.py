#Coffee Machine Project

from data import MENU, resources
import os

def report():
    print(f'''
    Water: {resources['water']}ml
    Milk: {resources['milk']}ml
    Coffee: {resources['coffee']}g
''')
    
def get_coins():
    print('Please insert coins.')
    quarter = float(input('How many quarters: ')) * 0.25
    dimes = float(input('How many dimes: ')) * 0.1
    nickles = float(input('How many nickles: ')) * 0.05
    pennies = float(input('How many pennies: ')) * 0.01 
    total = quarter + dimes + nickles + pennies
    return total


def check_resources(answer):
    can_make = 1
    for ingredient in MENU[answer]['ingredients']:
        if MENU[answer]['ingredients'][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            can_make = 0
    return can_make


while True:
    answer = input("\nWhat would you like? (espresso/latte/cappuccino/report):  ").lower()
    if answer == 'espresso' or answer == 'latte' or answer == 'cappuccino':
        if check_resources(answer) == 0:
            pass
        else: 
            total = get_coins()
            if total < MENU[answer]['cost']:
                print("Not enough money, coins refunded.\n")
            else:
                print(f"Total change: {total - MENU[answer]['cost']:.2f}")
                print(f"Here is your {answer}. Enjoy! ☕")
                for ingredient in MENU[answer]['ingredients']:
                    resources[ingredient] -= MENU[answer]['ingredients'][ingredient]

    elif answer == 'report': report()
    elif answer == 'off': exit("Machine Shutting Down...")
    else: print("\nInvalid Input.")
