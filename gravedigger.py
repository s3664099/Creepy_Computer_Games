#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: Gravedigger
Author: Alan Ramsey
Translator: David Sarkies
Version: 0
Date: 18 August 2023
Source: https://ia601902.us.archive.org/3/items/Creepy_Computer_Games_1983_Usborne_Publishing/Creepy_Computer_Games_1983_Usborne_Publishing.pdf
This game can be found on page 10 of Creepy Computer Games, and it a python3 translation.

"""

instructions = "It's dark and windy - not the kind of night to be lost in a graveyard, but\n"
instructions = "{}that's where you are. You have until midnight to find your way out. Skeletons\n".format(instructions)
instructions = "{}lurk in the shadows waiting to scare you to death should you get too close.\n".format(instructions)
instructions = "{}You can dig holes to help keep them away but digging is tiring work and\n".format(instructions)
instructions = "{}and you cannot manage more than five in one game. You have to be careful\n".format(instructions)
instructions = "{}not to fall down the holes you have dug too.\n".format(instructions)
instructions = "{}Grave stones (marked +) and the walls of the graveyard (marked :) block\n".format(instructions)
instructions = "{}your way. The holes you dig are marked 0 and you are * and the Skeletons\n".format(instructions)
instructions = "{}are *. See if you can escape.".format(instructions)

holes = 5
player = "*"
stone = "+"
hole = "O"
wall = ":"
skeleton = "X"
space = " "

def main_game():
	board = create_board()

	display = ""
	"""
	for x in range(10):
		for y in range(20):
			display += board[x][y]
		display += "\n"
	print(display)
	"""
def create_board():

	board = [[0 for x in range(20)] for y in range(10)] 

	for x in range(10):
		for y in range(20):
			board[x][y] = " "

	return populate_board(board)

def populate_board(board):

	for x in range(20):
		board[0][x] = wall
		board[9][x] = wall

	for x in range(10):
		board[x][0] = wall
		board[x][19] = wall

	return board




#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Starship Takeoff",sys.modules[__name__])