#!/usr/bin/env python3

import loader
import sys
import util
import time
import gravedigger_setup as setup
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

def main_game():

	finished = False
	board = setup.create_board()

	#Main Loop
	while not finished:
		display_board(board)
		action = get_action()

		if action == 'Q':
			finished = True
		else:
			process_action(action,board)

def display_board(board):

	display = ""
	util.clear_screen()

	for x in range(10):
		for y in range(20):
			display += board[x][y]
		display += "\n"

	print(display)

#Main input for the game
def get_action():

	correct = False
	entry = ""

	#Checks if the action is correct
	while not correct:
		print()
		print("You can go N,S,E, or W")
		print("[Q]uit or [D]ig")
		action = input("Enter Move: ")
		entry = action[0].upper()

		if entry not in ['N','S','E','W','Q','D']:
			print ("Please enter N,S,E, W, Q or D")
		else:
			correct = True

	return entry

#Checks result of action
def process_action(action,board):

	position = setup.player_position
	new_position = ()

	#Processes movement
	if action == "N":
		new_position = (position[0]-1,position[1])
	elif action == "S":
		new_position = (position[0]+1,position[1])
	elif action == "E":
		new_position = (position[0],position[1]+1)
	else:
		new_position = (position[0],position[1]-1)

	#Gets what is on the next position
	old_space = board[position[0]][position[1]]
	next_space = board[new_position[0]][new_position[1]]

	#Checks if it is a valid move
	if next_space in [setup.wall,setup.stone]:
		print("That way is blocked")
		time.sleep(2)
	elif new_position == (8,19):
		print("You have escaped")
		time.sleep(2)
	else:
		board[position[0]][position[1]] = setup.space
		board[new_position[0]][new_position[1]] = setup.player
		setup.player_position = new_position




#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Gravedigger",sys.modules[__name__])