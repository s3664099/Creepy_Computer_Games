#!/usr/bin/env python3

import loader
import sys
import util
from random import randint
import time

"""
Title: Mad House
Author: Keith Campbell
Translator: David Sarkies
Version: 0.1
Date: 
Source: https://ia601902.us.archive.org/3/items/Creepy_Computer_Games_1983_Usborne_Publishing/Creepy_Computer_Games_1983_Usborne_Publishing.pdf
This game can be found on page 12 of Creepy Computer Games, and it a python3 translation.

In this game you control two doors, and you have to line it up with the third, that will move randomly every twenty-five turns.
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
	finished = 0
	
	#Main game loop
	while (finished == 0):
		display(footsteps,width,door_position)
		print(door_direction)
		action = get_action()
		if (action != 'q'):
			door_direction = process_action(action,door_direction)
		else:
			finished = 3

		door_position = move_doors(door_position,door_direction,width,footsteps)
		footsteps -=1
		finished = check_results(finished,footsteps,door_position)

	end_game(finished)

#Displays the screen
def display(footsteps,width,door_position):

	util.clear_screen()
	print(footsteps)
	for x in range(3):
		print(display_walls(width,door_position[x]))
		print()

	#Commands
	print("\t\tx <-   Top Wall  -> c")
	print("\t\tm <- Bottom Wall -> n")
	print("\t\t\tq - quit")


#Builds each of the doors and positions them
def display_walls(width,door):

	line = "\t"

	for x in range(width):

		if (x==door):
			line = "{} ".format(line)
		elif (x==door-1):
			line = "{}>".format(line)
		elif (x==door+1):
			line = "{}<".format(line)
		else:
			line = "{}*".format(line)

	return line

#Function to get user command
def get_action():

	action = util.input_with_timeout_no_comment("",2)
	return action

#Processes the player action
def process_action(action,door_direction):

	if (action =="x"):
		door_direction[0] = -1
	elif (action == "c"):
		door_direction[0] = 1
	elif (action == "m"):
		door_direction[2] = -1
	elif (action == "n"):
		door_direction[2] = 1

	return door_direction

def move_doors(door_position,door_direction,width,footsteps):

	#Checks if the doors have reached the end of the row
	#If not, moves the door in the set directions
	if (((door_position[0]>1) and door_direction[0]==-1) 
		or ((door_position[0]<width-2) and door_direction[0]==1)):
		door_position[0] += door_direction[0]
	if (((door_position[2]>1) and (door_direction[2] == -1)) 
		or ((door_position[2]<width-2) and (door_direction[2]==1))):
		door_position[2] += door_direction[2]

	#Middle door moves every 5 moves. If it moves
	#beyond the width it goes back to the beginning
	if (footsteps/25==int(footsteps/25)):
		door_position[1] +=randint(0,20)-10

		if (door_position[1] >width-2):
			door_position[1] = 2 

	return door_position
	

#Checks if the game has ended.
def check_results(finished,footsteps,door_position):

	if (footsteps == 0):
		finished = 1
	elif ((door_position[0] == door_position[1]) and (door_position[1] == door_position[2])):
		finished = 2

	return finished	

def end_game(finished):

	if (finished == 1):
		print("Too Late! The footsteps have stopped")
		print("AGGGHHHH!!!!")
	elif (finished == 2):
		print("You are free!")		

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Mad House",sys.modules[__name__])