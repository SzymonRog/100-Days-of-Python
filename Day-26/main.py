import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

while True:
    word = input("Enter a word: ").upper()
    letters = list(word)
    translated = None
    try:
        translated = [nato_alphabet_dict[letter] for letter in letters]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(translated)
        break







