#NATO Project 2

import pandas as pd

nato_dataframe = pd.read_csv("Day-30/NATO/nato_phonetic_alphabet.csv")

nato_dict = {row['letter']:row['code'] for (index, row) in nato_dataframe.iterrows()}


while True:
    word = input("Enter a word: ").upper()

    try:
        result = [nato_dict[letter] for letter in word]
        
    except KeyError:
        print("Please only input letters.")

    else:
        print(result)
        break