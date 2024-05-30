#Calculator Project
from art import logo
import os

clear = lambda: os.system('cls')


def add (n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate():

    num1 = float(input("What is the first number?  "))

    while True:
        for operation in operations:
            print(f"{operation} ", end="")
        operator = input("Pick an operation  ")
        num2 = float(input("What is the next number?  "))

        for operation in operations:
            if operator == operation:
                result = operations[operation]
                final_result = result(num1, num2)

        print(f"{num1} {operator} {num2} = {final_result}")

        keep_going = input(f"Do you want to keep calculating with {final_result}? (1 - Yes/ 2 - No / 3 - Exit)  ")
        if keep_going == '1':
            num1 = final_result
        elif keep_going == '2':
            clear()
            calculate()
        else:
            exit("\nProgram Ended.\n")

print(logo)
calculate()