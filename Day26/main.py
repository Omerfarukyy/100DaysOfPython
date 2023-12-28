with open("file1.txt") as file1:
    f1 = file1.read().splitlines()
with open("file2.txt") as file2:
    f2 = file2.read().splitlines()
print(f1)
print(f2)
result = [n for n in f1 if (n not in f2)]

print(result)


sentence = input("Write a sentence: ")
length_of_words = {word: len(word) for word in sentence.split()}
print(length_of_words)

weather_c = eval(input())
print(weather_c)
weather_f = {key: (value * 9/5 + 32) for (key, value) in weather_c.items()}
print(weather_f)


