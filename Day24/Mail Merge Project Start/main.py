with open("./Input/Letters/starting_letter.txt") as file:
    blueprint = file.read()

with open("./Input/Names/invited_names.txt") as name:
    names = name.read().splitlines()
for n in names:
    with open(f"./Output/ReadyToSend/for_{n}.txt", "a") as answer:
        answer.write(blueprint.replace("[name]", n))

