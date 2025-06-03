#TODO: Create a letter using starting_letter.txt
#from gi.overrides.GObject import new_name

with open("Input/Names/invited_names.txt") as f:
    names = f.readlines()
for name in names:

    new_name= name.strip()

    with open("Input/Letters/starting_letter.txt") as letter:

        content = letter.read()

        text_in_letter = content.replace("[name]", new_name)
    with open(f"letter_{new_name}.txt", mode="w") as finish:
        finish.write(text_in_letter)

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp