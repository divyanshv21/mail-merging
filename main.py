
PLACEHOLDER = "[name]"

with open("/Users/divyanshverma/Downloads/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("/Users/divyanshverma/Downloads/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

    with open(f"/Users/divyanshverma/Documents/practice/python/MailMerging/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as output_file:
        output_file.write(new_letter)
