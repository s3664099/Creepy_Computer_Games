#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: Ghost Guzzler
Author: Colin Reynolds
Translator: David Sarkies
Version: 0
Date: 5 August 2023
Source: https://ia801902.us.archive.org/3/items/Creepy_Computer_Games_1983_Usborne_Publishing/Creepy_Computer_Games_1983_Usborne_Publishing.pdf
This game can be found on page 6 of Creepy Computer Games, and it a python3 translation.

This came is sort of an arcade game where you have to match the number that is approaching you. You 
can only increase it, and when you are matching it you attempt to guzzle it. If you do it before the
ghost (number) reaches you, then you get points based on the distance. Otherwise you lose a life.

I have added the score so you can see it as you are playing.

You can change the ease of the game by raising or lowering the speed (lower the faster, and it doesn't
need to be an integer). You can also change the difficulty by changing the max_distance (lower, harder).

"""

instructions = "The ghosts in this game are numbers rushing across the screen. To catch them,\n"
instructions = "{}you activate your ghost guzzler by pressing key X, but it only works when the\n".format(instructions)
instructions = "{}number on it is the same as that of the attacking ghost. You can increase the\n".format(instructions)
instructions = "{}guzzler's number by pressing key M (when it gets to 9, it goes back to 0 again).\n".format(instructions)
instructions = "{}If you fail to guzzle a ghost, it will snatch away one of your lives (shown as\n".format(instructions)
instructions = "{}/ top left of the screen). See how  good you are at guzzling ghosts.\n".format(instructions)

def main_game():

	score = 0
	number = 0
	lives = 3
	ghost_number = randint(0,9)
	distance = 1
	living = True
	speed = 1
	max_distance = 18

	while (living == True):

		got_ghost = False
		util.clear_screen()
		print_lives(lives,score)
		display_position(ghost_number,number,distance,max_distance+1)

		keypress = util.input_with_timeout_no_comment("",speed)

		got_ghost,number = check_keypress(keypress,number,ghost_number)

		#Checks if you got the ghost
		if (got_ghost == True):

			#Increases score and resets
			distance = 1
			score = score + (max_distance-distance)
			ghost_number = randint(0,9)

		else:
			distance += 1

			#Ghost got you
			if (distance==max_distance):
				lives -= 1
				distance = 1
				ghost_number = randint(0,9)

			#Out of lives
			if (lives == 0):
				living = False

#Processes the keypress
def check_keypress(keypress,number,ghost_number):

	got_ghost = False

	#Increases the number - do the opposite to add a command to lower the number
	if keypress == "m":

		number +=1

		if (number == 10):
			number = 0

	#Guzzle Attempt	
	elif keypress == "x":

		#Checks if the  numbers match
		if number == ghost_number:
			print("Got It")
			print("******")
			got_ghost = True

	return got_ghost,number

def display_position(ghost_number,number,distance,max_distance):

	first_distance = ""
	second_distance = ""

	# Define the format string with placeholders for the values
	for x in range (distance):
		first_distance += "  "

	for x in range (max_distance-distance):
		second_distance += "   "

	# Print the resulting text
	print("{}{}{}:{}".format(first_distance,ghost_number,second_distance,number))

def print_lives(lives,score):

	life_display=""

	for x in range(lives):
		life_display+="/ "

	print("{} Score: {}".format(life_display,score))
	print("\n\n\n")

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Ghost Guzzler",sys.modules[__name__])