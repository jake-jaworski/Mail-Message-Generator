
names_list = []


def create_names_list():
    final_list = []
    with open("Input/Names/invited_names.txt") as names:
        name_list = names.readlines()
        for name in name_list:
            final_list.append(name.strip())
    return final_list



def extract_text():
    with open("Input/Letters/starting_letter.txt") as letter:
        contents = letter.read()
        return contents


def add_name(name, contents):
    letter_text = contents.replace("[name]", name)
    return letter_text


def create_letter(name, letter_text):
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter:
        letter.write(letter_text)


names_list = create_names_list()

for name in names_list:
    raw_text = extract_text()
    letter_text = add_name(name, raw_text)
    create_letter(name, letter_text)
