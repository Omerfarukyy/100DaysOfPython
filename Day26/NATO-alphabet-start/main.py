import pandas

phonetic_alphabet_list = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_alphabet_list.iterrows()}
print(phonetic_dict)

while True:
    try:
        word = input().upper()
        output = [phonetic_dict[letter] for letter in word]
        break
    except KeyError:
        print("Please enter a valid text")
print(output)