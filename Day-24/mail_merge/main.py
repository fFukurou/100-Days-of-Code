#Mail Merge Project

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_list = []

with open(f"Day-24/mail_merge/Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

with open(f"Day-24/mail_merge/Input/Names/invited_names.txt") as file:
    names_list = file.readlines()

""" print(starting_letter)
for name in names_list:
    print(name.strip()) """

for name in names_list:
    with open(f"Day-24/mail_merge/Output/ReadyToSend/letter_for_{name.strip()}.txt", 'w') as file:
        final_letter = starting_letter.replace("[name]", f"{name.strip()}")
        file.write(f"{final_letter}")

