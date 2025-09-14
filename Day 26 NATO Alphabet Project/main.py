

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")
df_dict = {row.letter:row.code for (index,row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter your word\n").upper()

phonetic = [df_dict[letter] for letter in word if letter in df_dict ]
print(phonetic)
