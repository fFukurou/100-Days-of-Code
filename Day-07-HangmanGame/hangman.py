#Hangman Game Project
import random
from stages_ascii import stages
from words import word_list
import os

#Clears console
clear = lambda: os.system('cls')

#Gets random word from list
random_index = random.randint(0, len(word_list) - 1)
random_word = word_list[random_index].lower()
original_word = word_list[random_index]

tries = 7

user_guesses = []
display = []

#Transforms items from the list into chars and prints them
def print_word():
    for i in display:
        print(f"{i} ", end='')
    print("\n")
    
#Adds "_" to the display list based on the number of the letters of the random word
for i in random_word:
     display.append("_")


print_word()
print(f"You have {tries} tries. \n")

#Keeps the game running until player runs out of tries
while tries > 0:
    #Gets the guess and adds it to the user_guesses list
    while True:
        guess = input("Type a letter: ").lower()
        clear()
        if guess not in user_guesses:
            user_guesses.append(guess)
            break
        else:
            print("Repeated Guess. Please choose another letter.\n")
            print_word()

    #Checks whether the guess was correct or not. If True, assigns the guess to the correct spot in the display list. If False, diminishes the tries variable by one.
    if guess in random_word:
        print("\nCorrect guess.\n")
        print(stages[tries - 1])
        for i, letter in enumerate(random_word):
            if letter == guess:
                display[i] = original_word[i]
    else:
        print(f"Wrong! You have {tries - 1} more tries")    
        print(stages[tries - 1])
        tries -=1

    print_word()

    #If there are no more "_" in the display, then there are no more unguessed letters, meaning the player won.
    if "_" not in display:
        exit("You won!")
        
#If tries gets to 0, this code will be executed, ending the game.
exit("You got hanged.")