#NATO Project

import pandas as pd
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

nato_dataframe = pd.read_csv("Day-26-NATO/NATO/nato_phonetic_alphabet.csv")

nato_dict = {row['letter']:row['code'] for (index, row) in nato_dataframe.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input = input("Enter a word: ").upper()

result = [nato_dict[letter] for letter in input]
print(result)