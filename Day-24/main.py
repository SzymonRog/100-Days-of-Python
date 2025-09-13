#Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

names = []
letter = ""

with open("./Input/Letters/starting_letter.txt", "r") as file:
    letter = file.read()

with open("./Input/Names/invited_names.txt", "r") as file:
    for name in  file.readlines():
        names.append(name.strip())


for name in names:
    new_letter = letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        file.write(new_letter)

