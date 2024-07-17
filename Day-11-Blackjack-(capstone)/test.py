user_hand = [11, 22, 33]
user_score = 22

if 11 in user_hand and user_score > 21:
    index = user_hand.index(11)
    user_hand[index] = 1
print(user_hand)


##
#BlackJack Project
import random
from art import logo
import os

clear = lambda: os.system('cls')



def deal_cards():
    random_card = random.randint(0, len(cards) - 1)
    return cards[random_card]

def check_blackjack():
    if len(user_hand) == 2 and user_score == 21 and len(dealer_hand) == 2 and dealer_score == 21:
        return 2
    elif len(user_hand) == 2 and user_score == 21:
        return 0
    elif len(dealer_hand) == 2 and dealer_score == 21:
        return 1

def update_score():
    global user_score 
    global dealer_score
    user_score = sum(user_hand)
    dealer_score = sum(dealer_hand)

    if 11 in user_hand and user_score > 21:
        index = user_hand.index(11)
        user_hand[index] = 1
        user_score = sum(user_hand)

    if 11 in dealer_hand and dealer_score > 21:
        index = dealer_hand.index(11)
        dealer_hand[index] = 1
        dealer_score = sum(dealer_hand)


def check_first_hand():
    if check_blackjack() == 0: 
        return 'Blackjack Win!'
    elif check_blackjack() == 1:
        return 'Blackjack Loss'
    elif check_blackjack() == 2:
        return 'Blackjack Draw!'

def compare(user_score, dealer_score):
    if user_score > 21 and dealer_score > 21: return 'Draw!'
    elif user_score > 21: return 'Loss!'
    elif dealer_score > 21:return 'Win!'

def print_score():
    print(f"Your Cards: {user_hand}, Current score: {user_score}")
    print(f"Dealer's First Card: {dealer_hand[0]}")

def print_final_score():
    print(f"Your Final Hand: {user_hand}, Final Score: {user_score}")
    print(f"Dealer's Final Hand {dealer_hand}, Final Score {dealer_score}\n")

def game_end_check():
    if user_score == dealer_score: return "Draw!"
    elif user_score > dealer_score: return "Win!"
    elif user_score < dealer_score: return "Loss!"


while True:
    asnwer = input("Do you want to play a game of Blackjack? (Y/N)  ").lower()
    if asnwer == 'n':
        exit("Thank you for playing. ")

    clear()
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_hand = []
    dealer_hand = []

    user_score = 0
    dealer_score = 0

    for i in range(0,2):
        user_hand.append(deal_cards())
        dealer_hand.append(deal_cards())

    update_score()
    if check_first_hand() is not None:
        print_final_score()
        print(check_first_hand())

    else:
        while True:
            print_score()
            another_card = input("Type 'y' to get another card, type 'n' to pass:  \n\n")
            if another_card == 'y':
                user_hand.append(deal_cards())
                update_score()
                if compare(user_score, dealer_score) is not None:
                    print_final_score()
                    print(compare(user_score, dealer_score))
                    break

            elif another_card == 'n':
                while dealer_score < 17:
                    dealer_hand.append(deal_cards())
                    update_score()

                if compare(user_score, dealer_score) is not None:
                    print_final_score()
                    print(compare(user_score, dealer_score))
                    break

                print_final_score()
                print(game_end_check())
                break
            