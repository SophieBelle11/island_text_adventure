
yes_no = ["yes", "no"]
directions = ["left", "right", "climb", "jungle", "coast","go back"] 

# Introduction
print("""
Welcome to Sophie's first Text Based Adventure Game! Have fun!!
""")

name = input:("Hello weary traveller, what is your name?\n")
print("Greetings, "(name)" You have awoken on a deserted island, covered in pink sand with terquoise waters shinning off the coast.")
print("You see a verdant jungle meeting the beach to your left and tall cliffs further away on the right.")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Do you dare start exploring?\nyes/no\n")
    if response == "yes":
        print("Which direction do you go in first?\nleft to jungle/right to forest")
    elif response == "no":
        print("Ah" + name + "I didn't realize you are a coward")
    else: 
        print("What? Are you daft?")
        


