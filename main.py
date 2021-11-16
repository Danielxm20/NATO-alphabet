import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_data_frame = pandas.DataFrame(data)
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}
print(nato_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Type the word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()