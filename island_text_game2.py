from time import time

import time
from turtle import back

yes = {"yes", "y", "yeah", "yep", "hike"}
no = {"no", "N", "No"}
directions = ["left", "right", "go back"]
fight = ["fight"]
jump = ["jump"]
take = ["take"]
refuse = {"refuse","no"}
take = {"take", "accept", "yes"}
coast = {"coast", "right"}
cliffs = {"cliffs", "yes"}
jungle = {"jungle", "left"}
stop = {"stop", "admire", "yes"}
hike = {"hike," "yes"}


"""
RECOMMENDATIONS:

Install Code Spell Checker extension
Use sets, not arrays
Set all input to .lower() to check
When checking, check against set, "if response in set" 
Maybe put a space or newline at the end of inputs

"""

# Helper function to print strings formatted as a paragraph
def print_paragraph(string):
	print(f"\n%s\n"%string)

# print("""

# Welcome to Sophie's first Text Based Adventure Game! Have fun!!

# """)
print_paragraph("Welcome to Sophie's first Text Based Adventure Game! Have fun!!")

time.sleep(1.0)
name = input("Hello brave traveler, what is your name?\n\n")
print("Ah, " + name + ", that's a good name.")
time.sleep(1.0)
print("Well, " + name + ", tell me...")
time.sleep(1.0)
begin = input("... are you ready to start your adventure?\n\n").lower()
while (True):
	if begin in yes: 
		print_paragraph("You've awoken with nothing but the clothes on your back, on a deserted island. You are surrounded by soft pink sand, you can see beautiful turquoise waters off the coast. Off to your left you see a verdant jungle that goes deeper into the island, on your right a beach that leads to a wall of sea cliffs.\n\n")
	elif begin in no: 
		print("\nOh, I did not realize you were a coward " + name)
		time.sleep(0.5)
		print("... How disappointing.")
		quit()
	else:
		print("\nUm... okay " + name)
		time.sleep(2.0)
		begin = input("... are you ready to start your adventure?\n\n").lower()
	

#Starting the Adventure
	time.sleep(0.5)	
	choose = input("Where do you head, left towards the jungle or right along the coast?\n\n").lower()

#Jungle Adventure Plot
	if choose in jungle:
		print_paragraph("You venture deeper into the island towards the jungle, the trees are even more enormous than they appeared from the beach. There is no clear path through but you find the ancient and undisturbed nature of this place peaceful.")
		stay = input("Do you continue to explore the jungle?\n\n").lower()
		if stay == 'yes':
				print_paragraph("Birds caw above as you push further through the overgrowth. Eventually to you come to a tree with mysterious hand holds secured into the trunk.")
				climb = input("Do you dare climb the tree?\n\n").lower()
				if climb == 'yes':
					print_paragraph("Your curiosity compels you to climb the tree, arriving at the top you see a wide stretch of rope bridges winding through the jungle canopy. Amazed and growing ever more curious, you continue down the most secure looking of the rope bridges.")				
					time.sleep(2.0)
					print_paragraph("The sounds of the jungle below you and the freedom you feel crossing each bridge from tree to tree wells up a feeling joy you haven't experienced in ages.")
					time.sleep(2.0)
					print_paragraph("Soon, in the distance you see rows of tree houses, but you noticed too late and were spotted first!")
					time.sleep(2.0)
					print_paragraph("Before you can move a muscle you are surrounded by a tribe of jungle tree dwellers, wielding spears and bows already notched. All weapons are pointed directly at you. The options to survive are slim. You can stand and fight or take your chances jumping into the jungle below...")
					survive = input("Do you stand and fight or jump?\n\n").lower()
					if survive == 'fight':
						print("\nYou take a fighting stance and are quickly speared and shot by the tree warriors")
						time.sleep(1.0)
						print(name +" you slowly bleed out and die painfully, with nothing but the gorgeous view from the canopy to give you solace.")
						quit()
					elif survive == 'jump':
						time.sleep(0.5)
						print_paragraph("Steeling your nerves you prepare to jump into the jungle below, hoping some plants may break your fall.")
						time.sleep(1.0)
						print_paragraph("You launch yourself but are pulled back by the tribe. Upon seeing you would rather plunge to your death than attack the tree people, they realize you mean no harm and have saved you.")
						time.sleep(3.0)
						print_paragraph("A beautiful woman, dressed in garb that could only indicate a role of high honor or power, steps forward.")
						time.sleep(3.0)
						print("\nShe reaches up into the trees, grabbing a coconut, she breaks it in half with her bare hands!")
						time.sleep(1.0)
						print("\nShe offers you half")
						live = input("Do you take it or refuse?\n\n").lower()
					if live in take:
						print_paragraph("You accept the coconut and the woman leads the tribe in a cheer, the group takes you to the nesting of shelters. They give you food, water and your own tree house! The tribe shows you their ways of surviving in the jungle. You adapt to this new way of life. Although it is not the home you originated from. You are happy.")
						time.sleep(2.0)
						print(name + ", you have been adopted by the tree people. Congratulations on your new life.")
						quit()
					elif live in refuse:
						print_paragraph("Your refusal angers the woman and with a flick of her wrist she commands the warriors to forcefully push you off the precarious rope bridge.")
						print("You fall and hit the jungle floor with an impact that breaks every bone in your body, unable to move you lie there in agony, wondering what will become of you now.")
						time.sleep(1.0)
						print_paragraph("As dawn breaks a strange crab scuttles into view, but quickly darts off. You are concerned but can do nothing.")
						time.sleep(3.0)
						print("It matters not for the crab returns with a group that encircles you.")
						time.sleep(2.0)
						print(name + ", you are eaten alive by coconut crabs")
						quit ()

				elif climb == 'no':
					time.sleep(1.0)
					print_paragraph("Unnerved by this discovery, you turn to leave but suddenly feel a sharp pain in your shoulder")
					time.sleep(0.5)
					print("\nYou have been shot by an arrow from an unknown attacker. As the world fades around you, you realize the arrow must be poisoned.")
					time.sleep(0.5)
					print(name + " you have died. At least it was a quick death.")
					quit()

		elif stay == 'no':
			time.sleep(0.5)
			print_paragraph("You head back towards the beach.")
			time.sleep(2.0)
			choose = input("Where do you head, left towards the jungle or right along the coast?\n\n").lower()

				

#Coastal Cliffs Plot			
	elif choose in coast:
		print_paragraph("You follow the coast towards the cliffs, as you get closer you realize they are a similar pink color to the sand on the beach. You notice nature has eroded a path to hike up the cliffs.")
		up = input("Do you hike up the cliffs?\n\n").lower()
		if up == 'yes':
			print_paragraph("You start heading up the cliffs, hoping to get a better view of this island you've been stranded on. As you get closer to the top you reach a stunning overlook.")
			stop = input("Would you like to stop and admire the view?\n\n").lower()
			if stop == 'yes':
				time.sleep(0.5)
				para = ("You approach the overlook, the incredible view of the coastal waters becoming ocean overwhelms you."
				"The beauty of the horizon line where ocean meets sky is tainted by the realization of just how isolated you are."
				)
				print_paragraph(para)
		elif up == 'no':
			time.sleep(0.5)
			print_paragraph("You turn around and walk back to the beach")
			time.sleep(2.0)
			choose = input("Where do you head, left towards the jungle or right along the coast?\n\n").lower()
		else: print("Well come on now, you can't just sit here, " + name +".")
		break





	print("What are ya daft?") 
	

        

	




