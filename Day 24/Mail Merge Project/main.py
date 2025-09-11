#TODO: Create a letter using starting_letter.txt

names = open(r"./Input/Names/invited_names.txt",'r')
names_list = names.readlines()
#for each name in invited_names.txt
for name in names_list:
    name = name.strip()
    with open(r"./Input/Letters/starting_letter.txt") as file:
        s_letter = file.read()
    with open(fr"./Output/ReadyToSend/{name}_letter.txt",mode="w") as file:
        #We have the name from the name files
        updated_letter = s_letter.replace("[name]",name) # Replacing the [name] with the name from the list
        letter = file.write(updated_letter) #Creating a new letter

