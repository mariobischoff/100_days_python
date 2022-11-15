import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (_, row) in nato_df.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    word_list = [letter for letter in word]
    try:
        phonetic = [nato_dict[letter] for letter in word_list]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(phonetic)


generate_phonetic()