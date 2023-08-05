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

	util.clear_screen()
	print_lives(lives)
	display_position(ghost_number,number,distance)

def display_position(ghost_number,number,distance):

	first_distance = ""
	second_distance = ""

	# Define the format string with placeholders for the values
	for x in range (distance):
		first_distance += "  "

	for x in range (19-distance):
		second_distance += "   "

	# Print the resulting text
	print("{}{}{}:{}".format(first_distance,ghost_number,second_distance,number))

def print_lives(lives):

	life_display=""

	for x in range(lives):
		life_display+="/ "

	print(life_display)
	print("\n\n\n")

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Ghost Guzzler",sys.modules[__name__])