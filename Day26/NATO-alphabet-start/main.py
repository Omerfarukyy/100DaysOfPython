import pandas

word = input()
phonetic_alphabet_list = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_list = {}
for (index, row) in phonetic_alphabet_list.iterrows():
    new_dict = {row.letter: row.code for item in row}
    alphabet_list.update(new_dict)

result = [alphabet_list[letter] for letter in word.upper()]
print(result)
