PLACEHOLDER = "[name]"
        
with open("/Users/kyleleonard/100-Days-Of-Code_Python/day-24/Input/Names/invited_names.txt") as names_file:
   names = names_file.readlines()
   print(names)
   
with open("/Users/kyleleonard/100-Days-Of-Code_Python/day-24/Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"/Users/kyleleonard/100-Days-Of-Code_Python/day-24/Output/ReadyToSend/letter_for_{stripped_name}", mode="w") as completed_letter:
            completed_letter.write(new_letter)