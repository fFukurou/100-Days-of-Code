#Blind Auction Project

from art import logo
import os

clear = lambda: os.system('cls')

print(logo)

list_of_bidders = []
highest_bid = {'name': "", 'bid': 0}


print("Welcome to the secret auction program.")
while True:
    name = input("What is your name?  ")
    bid = int(input("What is your bid?  "))

    list_of_bidders.append({
        'name': name,
        'bid': bid,
    })

    other_bidders = input("Are there any other bidders? (yes/no) ")
    if other_bidders == "no":
        break
    else: 
        clear()

for person in list_of_bidders:
        if person['bid'] > highest_bid['bid']: highest_bid['name'], highest_bid['bid'] = person['name'], person['bid']

print(f"The winner is {highest_bid['name']} with a bid of {highest_bid['bid']}")