#BlackJack Project
import random
from art import logo
import os

clear = lambda: os.system('cls')


#Appends a random card to a list (hand)
def deal_cards(hand):
    random_card = random.randint(0, len(cards) - 1)
    hand.append(cards[random_card])
    update_score()

#Checks if there is blackjack in play (Cards 10 and 11)
def check_blackjack():
    if len(user_hand) == 2 and user_score == 21 and len(dealer_hand) == 2 and dealer_score == 21:
        return "BlackJack Draw!"
    elif len(user_hand) == 2 and user_score == 21:
        return "BlackJack Win!"
    elif len(dealer_hand) == 2 and dealer_score == 21:
        return "BlackJack Loss!"

#Updates the scores and if one of the players has an ACE (11), it becomes a 1 if the scores goes above 21
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


#Checks if one of the scores exceeded 21
def compare(user_score, dealer_score):
    if user_score > 21 and dealer_score > 21: return 'Draw!'
    elif user_score > 21: return 'Loss!'
    elif dealer_score > 21: return 'Win!'

#If one of scores exceeded 21, prints the final score and returns True to activate the break in the main loop
def check_21():
    if compare(user_score, dealer_score) is not None:
        print_final_score()
        print(compare(user_score, dealer_score))
        return True

#Prints the score and dealer's first card
def print_score():
    print(f"Your Cards: {user_hand}, Current score: {user_score}")
    print(f"Dealer's First Card: {dealer_hand[0]}")

#Prints the final score. Used only when the game is over
def print_final_score():
    print(f"Your Final Hand: {user_hand}, Final Score: {user_score}")
    print(f"Dealer's Final Hand {dealer_hand}, Final Score {dealer_score}\n")

#Checks which player has the highest score (If no scores exceeded 21 and there was no blackjack)
def game_end_check():
    if user_score == dealer_score: return "Draw!"
    elif user_score > dealer_score: return "Win!"
    elif user_score < dealer_score: return "Loss!"


#Main loop
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
       deal_cards(user_hand)
       deal_cards(dealer_hand)

    update_score()
    if check_blackjack() is not None:
        print_final_score()
        print(check_blackjack())

    else:
        while True:
            print_score()
            another_card = input("Type 'y' to get another card, type 'n' to pass:  \n\n")
            if another_card == 'y':
                deal_cards(user_hand)

                if check_21() is True:
                    break

            elif another_card == 'n':
                while dealer_score < 17:
                    deal_cards(dealer_hand)

                if check_21() is True:
                    break

                print_final_score()
                print(game_end_check())
                break
            