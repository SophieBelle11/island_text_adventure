from time import time

import time

yes = ["yes", "Y", "Yes"]
no = ["no", "N", "No"]
directions = ["left", "right", "go back"]
fight = ["fight"]
jump = ["jump"]
take = ["take"]
refuse = ["refuse"]
coast = ["coast"]
cliffs = ["cliffs"]
jungle = ["jungle"]

print("""

Welcome to Sophie's first Text Based Adventure Game! Have fun!!

""")
time.sleep(1.0)
name = input("Hello brave traveller, what is your name?\n")
print("Ah, " + name + ", that's a good name.")
time.sleep(1.0)
print("Well, " + name + ", tell me...")
begin = input("are you ready to start your adventure?\n")


if begin == 'yes' or 'Yes': 
	print("""

	You've awoken on a desert island surrounded by soft pink sand, you can see beautiful terquoise waters off the coast. Off to your left you see a verdant jungle that goes deeper into the island, on your right a beach that leads to a wall of sea cliffs.\n
	
	""")
elif begin == 'no' or 'No': 
		print("Oh, I did not realize you were a coward " + name + "... How disappointing.")
else:
		print("What are ya daft?")

#Starting the adventure
time.sleep(0.5)	
choose = input("Where do you head, left towards the jungle or right along the coast?")

#Jungle Adventure Plotline
if choose == 'left' or 'jungle':
			print("""
			
	You venture deeper into the island towards the jungle, the trees are even more enormous than they appeared from the beach. There is no clear path through but you find the ancient and undisturbed nature of this place peaceful.
			
			""")
			stay = input("Do you continue to explore the jungle?")
			if stay == 'yes':
					print("""
				
	Birds caw above as you push further through the overgrowth. Eventually to you come to a tree with mysterious hand holds secured into the trunk.
				
				""")
					climb = input("Do you dare climb the tree?")
					if climb == 'yes':
						print("""
						
	Your curiosity compells you to climb the tree, arriving at the top you see a wide strech of rope bridges winding through the jungle canopy. Amazed and growing ever more curious, you continue down the most secure looking of the rope bridges.
	
	""")				
						print("""
						
	The sounds of the jungle below you and the freedom you feel crossing each bridge from tree to tree wells up a feeling joy you haven't expirienced in ages. Soon, in the distance you see rows of tree houses, but you noticed too late and were spotted first! 
	
	Before you can move a muscle you are surrounded by a tribe of jungle tree dwellers, weilding spears and bows already notched. All weapons are pointed directly at you. The options to survive are slim. You can stand and fight or take your chances jumping into the jugle below"
	
	""")
						survive = input("Do you stand and fight or jump?")
						if survive == 'fight':
							print("""
							
	You take a fighting stance and are quickly speared and shot by the tree warriors.
	
	""")
							print(name +" you slowly bleed out and die painfully, with nothing but the gorgeous view from the canopy to give you solace.")
							quit()

						elif survive == 'jump':
							print("""
							
	Steeling your nerves you prepare to jump into the jungle below, hoping some plants may break your fall. You launch yourself but are pulled back by the tribe. Upon seeing you would rather plunge to your death than attack the tree people, they realize you mean no harm and have saved you.
	
	""")
						live = input("Do you take or refuse the coconut half?")
						if live == 'take':
							print("""
							
	You accept the coconut and the woman leads the tribe in a cheer, the group takes you to the row of treehouses. They give you food and shelter, your own treehouse! The tribe shows you their ways of surviving in the jungle. You adapt to this new way of life. Although it is not the home you originated from. You are happy.
							
							""")
							print(name + ", you have been adopted by the tree people. Congratulations on your new life.")
							quit()
						elif live == 'refuse':
							print("""

	Your refusal angers the woman and with a flick of her wrist she commands the warriors to forcefully push you off the percarious rope bridge.
	
	""")
							print("You fall and hit the jungle floor with an impact that breaks every bone in your body, unable to move you lie there in agony, wondering what will become of you now.")
							print("""
							
	As dawn breaks a strange crab scuttles into view, but quickly darts off. You are concerned but can do nothing, it matters not for the crab returns with a group that encircles you.
	
	""")
							print(name + ", you are eaten alive by coconut crabs")
							quit ()

					elif climb == 'no':
						print("""
						
	Unerved by this discovery, you turn to leave but suddenly feel a sharp pain in your shoulder. You have been shot by an arrow from an unknown attacker. As the world fades around you, you realize the arrow must be poisioned.
	
	""")
						print(name + " you have died")
						quit()

			elif stay == 'no':
					print("""
				
	You head back towards the beach.
				
				""")
					

#Coastal Cliffs Plotline			
elif choose == 'right' or 'coast':
			print("""
			
	You follow the coast towards the cliffs, as you get closer you realize they are a similar pink color to the sand on the beach. You notice nature has eroded a path to hike up the cliffs.
			
			""")
else: print("Well come on now, you can't just sit here, " + name)
	

        

	




