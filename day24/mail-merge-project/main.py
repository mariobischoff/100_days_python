with open("Input/Names/invited_names.txt") as file:
    content = file.read()
    names = content.split("\n")

with open("Input/Letters/starting_letter.docx") as file:
    letter: str = file.read()
    for name in names:
        new_letter = letter.replace("[name]", name)
        with open(f"Output/ReadyToSend/letter_for_{name}.docx", mode="w") as file:
            file.write(new_letter)