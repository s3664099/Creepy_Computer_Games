#!/usr/bin/env python3

import loader
import sys
import util
from random import randint
import time

"""
Title: 
Author: 
Translator: David Sarkies
Version: 0.1
Date: 
Source: https://ia601902.us.archive.org/3/items/Creepy_Computer_Games_1983_Usborne_Publishing/Creepy_Computer_Games_1983_Usborne_Publishing.pdf
This game can be found on page 12 of Creepy Computer Games, and it a python3 translation.
"""

instructions = "You're trapped in a weird house where everything moves including the walls. If\n"
instructions = "{}the doorways would line up, even for a moment, you could make a dash for\n".format(instructions)
instructions = "{}freedom. You've found a console which appears to control some of the\n".format(instructions)
instructions = "{}movements in the house. Keys X and C make the doorway nearest to you\n".format(instructions)
instructions = "{}(top of the screen) change direction. Keys N and M have the same effect\n".format(instructions)
instructions = "{}on the door way furthest from you. There doesn't seem to be any way for\n".format(instructions)
instructions = "{}controlling the centre doorway.".format(instructions)
instructions = "{}As you frantically wrestle with the knobs on the console, you can hear\n".format(instructions)
instructions = "{}footsteps pounding down the corridor behind you. The number top left\n".format(instructions)
instructions = "{}of the screen shows their progress towards you. If you can't escape\n".format(instructions)
instructions = "{} before the phantom footsteps catch up with you ...".format(instructions)

def main_game():
	width = 31
	footsteps = 240
	door_position = [randint(1,(width-4)+1),randint(1,(width-4)+1),randint(1,(width-4)+1)]
	door_direction = [1,0,-1]
	
	#Main game loop
	while (footsteps>0):
		display(footsteps,width,door_position)
		time.sleep(2)
		footsteps -=1

#Displays the screen
def display(footsteps,width,door_position):

	util.clear_screen()
	print(footsteps)
	for x in range(3):
		print(display_walls(width,door_position[x]))
		print()

#Builds each of the doors and positions them
def display_walls(width,door):

	line = ""

	for x in range(width):

		if (x==door):
			line = "{}> <".format(line)
		else:
			line = "{}*".format(line)

	return line


#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Mad House",sys.modules[__name__])