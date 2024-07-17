#Code Machine OOP Project

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
moneyMachine = MoneyMachine()

is_on = True

while is_on:
    answer = input(f"\nWhat would you like? ({menu.get_items()})  ").lower()

    if answer == 'latte' or answer == 'cappuccino' or answer == 'espresso':
        order = menu.find_drink(answer)
        if machine.is_resource_sufficient(order) is True:
            if moneyMachine.make_payment(order.cost) is True: #type: ignore
                machine.make_coffee(order)


    elif answer == 'report': machine.report()

    elif answer == 'off': 
        print("\nMachine Shutting Down...")
        is_on = False

    else: print("\nInvalid Input")