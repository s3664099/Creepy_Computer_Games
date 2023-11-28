#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: Sceance
Author: Chris Oxlade
Translator: David Sarkies
Version: 0
Date: 
Source: https://ia601902.us.archive.org/3/items/Creepy_Computer_Games_1983_Usborne_Publishing/Creepy_Computer_Games_1983_Usborne_Publishing.pdf
This game can be found on page 16 of Creepy Computer Games, and it a python3 translation.

"""

instructions = "Messages from the Spirits are coming through, letter by letter. They want you to\n"
instructions = "{}remember the letters and type them into the computer in the correct order. If\n".format(instructions)
instructions = "{}you make mistakes they will be angry - very angry ...\n".format(instructions)
instructions = "{}Watch for starts on your screen - they show the letters in the Spirit's\n".format(instructions)
instructions = "{}messages.".format(instructions)

characters = ["a","b","c","d","e","f","g","h"]

def title():
	spaces = util.tab(8,4)
	util.clear_screen()
	print("{}Sceance".format(spaces))
	position = get_position(7,5)

	for i in range(8):

		letter=characters[i]
		position = display_characters(letter,position)

	print(position)

def get_position(x,y):

	position = util.tab(x,2)
	for i in range(y):
		position = "\n{}".format(position)

	return position	

def display_characters(letter,position):

	display = "{}{}".format(position,letter)
	
	return display

def main_game():
	s=0
	g=0
	cs=64
	title()


#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Scence",sys.modules[__name__])