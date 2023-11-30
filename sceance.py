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

characters = ["a","b","c","d","e","f","g","h","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def title():
	spaces = util.tab(8,4)
	util.clear_screen()
	print("{}Sceance".format(spaces))

def set_position(x,y,letter):

	return {"x": x, "y": y,"Letter": letter}

def build_screen():

	positions = []

	for i in range(8):

		positions.append(set_position(5,6+i,characters[i]))
		positions.append(set_position(11,6+i,characters[19-i]))

	for i in range(5):

		positions.append(set_position(5+i,5,characters[24-i]))
		positions.append(set_position(5+i,16,characters[8+i]))

"""
	number = randint(4,7)
	letters = ""

	for i in range(number):
		star = "*"
		rand_letter = randint(0,26)
		letter = characters[rand_letter]
		letters = "{}{}".format(letters,letter)

		x=6
		y=rand_letter+6

		if rand_letter<22:
			y=10
			x=28-rand_letter
		elif rand_letter<14:
			x=15
			y=rand_letter-3
		else:
			y=64
			x=rand_letter+6
		positions.append(set_position(x,y,star))
"""
	#Display Screen
	#Pause
	#Replace With Blank
	#Get Quess
	#If Guess = letters correct
	#Else loose

def main_game():
	s=0
	g=0
	cs=64
	title()
	build_screen()

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Scence",sys.modules[__name__])