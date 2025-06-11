student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

#leemos el archivo csv y automaticamente nos devuelve un dataframe
alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

#utilizamos la comprension de diccionario y creamos un diccionaro con la letra y su codigo
phonetic_dict = {row.letter:row.code for (index, row) in alphabet_df.iterrows()}

#voy a tomar la entrada del usuario
user_phonetic = input("Type your name: \n").upper()

#agrego cada letra a una lista
user_phonetic_list = [let for let in user_phonetic]

#interpreto cada letra con cada codigo en phonetic_dict y lo agrego a una nueva lista "output_phonetic_name"
output_phonetic_name = [phonetic_dict[let] for let in user_phonetic_list]
print(output_phonetic_name)