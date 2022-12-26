#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp'


with open("./Input/Letters/starting_letter.txt", "r") as input_letter:
    input_letter_content = input_letter.read()
    print(input_letter_content)

with open("./Input/Names/invited_names.txt", "r") as input_names:
    names = [i for i in input_names.readlines()]
    names = list((map(lambda n: n.strip(), names)))
    print(names)

for i in names:
    with open(f"./Output/ReadyToSend/letter_to_{i}.txt", "w") as output_letter:
        letter = input_letter_content.replace("[name]", i)
        output_letter.write(letter)
