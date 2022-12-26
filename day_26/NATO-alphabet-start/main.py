import pandas as pd


df = pd.read_csv("nato_phonetic_alphabet.csv")
print(df.head())




#TODO 1. Create a dictionary in this format:
df_dict = {row.letter: row.code for index, row in df.iterrows()}
print(df_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Please enter your name: ").upper()
user_input_list = [i for i in user_input]
phonetic_code_words = [df_dict[i] for i in user_input_list]
print(phonetic_code_words)


