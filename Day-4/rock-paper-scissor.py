import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
possible_choices = [rock, paper, scissors]


bot_choice = random.randint(0, 2)

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice > 2 or player_choice < 0:
    exit("You typed an invalid number. Now you lose.")

print(possible_choices[player_choice])
print("\nComputer Chose:\n")
print(possible_choices[bot_choice])


if player_choice == bot_choice:
    print("\n Draw!")

elif player_choice == 0 and bot_choice == 1:
    print("\n You lost.")
    
elif player_choice == 0 and bot_choice == 2:
    print("\n You won.")

elif player_choice == 1 and bot_choice == 0:
    print("\n You won.")

elif player_choice == 1 and bot_choice == 2:
    print("\n You lost.")

elif player_choice == 2 and bot_choice == 1:
    print("\n You won.")

elif player_choice == 2 and bot_choice == 0:
    print("\n You lost.")
