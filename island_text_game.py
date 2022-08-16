yes = ["yes", "Y"]
no = ["no", "N"]
directions = ["left", "right", "go back"]

print("""

Welcome to Sophie's first Text Based Adventure Game! Have fun!!

""")
name = input("Hello brave traveller, what is your name?\n")
print("Ah, " + name + ", that's a good name.")
print("Well, " + name + ", tell me...")
begin = input("are you ready to start your adventure? (yes / no)")

if begin == 'yes': 
	print("You've awoken on a desert island surrounded by soft pink sand, you can see beautiful terquoise waters off the coast. Off to your left you see a verdant jungle that goes deeper into the island, on your right a beach that leads to a wall of sea cliffs.\n")
elif begin == 'no': 
	print("Oh, I did not realize you were a coward " + name + "... How disappointing.")
else:
	print("What are ya daft?")

	

        

	




