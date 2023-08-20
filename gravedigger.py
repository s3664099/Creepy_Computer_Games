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

def main_game():

	holes = 5
	score = 0
	finished = False
	board = setup.create_board()
	display_board(board)

	#Main Loop
	while not finished:

		result = 0
		action = get_action()
		score +=1

		if action == 'Q':
			finished = True
		elif action == 'D':
			holes = dig_hole(board,holes)
		else:
			result = process_action(action,board)
			result = move_skeletions(board,result)

		setup.place_holes(board)
		display_board(board)

		if result != 0:
			finished = True

	print(display_result(result,score,holes))

	reset_game()		

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
		print("[Q]uit, [D]ig, [X] (Do Nothing)")
		action = input("Enter Move: ")
		entry = action[0].upper()

		if entry not in ['N','S','E','W','Q','D','X']:
			print ("Please enter N,S,E, W, Q, D or X")
		else:
			correct = True

	return entry

#Checks result of action
def process_action(action,board):

	position = setup.player_position
	finished = 0

	new_position = process_move(action,position)

	#Gets what is on the next position
	old_space = board[position[0]][position[1]]
	next_space = board[new_position[0]][new_position[1]]

	#Checks if it is a valid move
	if next_space in [setup.wall,setup.stone]:
		print("That way is blocked")
		time.sleep(2)
	elif new_position == setup.exit:
		finished = 1
	elif next_space in [setup.hole]:
		finished = 2
	elif next_space in [setup.skeleton]:
		finished = 3
	else:
		board[position[0]][position[1]] = setup.space
		board[new_position[0]][new_position[1]] = setup.player
		setup.player_position = new_position

	return finished

#Processes the Dig Hole Action
def dig_hole(board,holes):

	#Checks if the player is able to dig any more holes
	if holes == 0:
		print('You are unable to dig anymore holes')
		time.sleep(2)

	#Creates a hole at the position selected
	else:
		holes -=1
		setup.hole_position.append(((setup.player_position[0]),(setup.player_position[1])))

	return holes

#Processes the skeleton's move
def move_skeletions(board,result):

	direction = ['N','S','E','W']

	skel_number = 0
	skeletons_removal = []

	for x in setup.skeleton_position:

		move_valid = False

		while not move_valid:

			#If the skeleton next to the player
			new_position = check_adjacent_square(x,board)

			#If not moves in a random direction
			if new_position == (-1,-1):
				new_position = process_move(direction[randint(0,3)],x)

			next_space = board[new_position[0]][new_position[1]]

			#Skeletons cannot leave the graveyard
			if new_position == setup.exit:
				move_valid = False 

			elif next_space not in [setup.wall,setup.stone,setup.skeleton]:
				move_valid = True
				board[x[0]][x[1]] = setup.space
				board[new_position[0]][new_position[1]] = setup.skeleton
				setup.skeleton_position[skel_number] = (new_position[0],new_position[1])

				#Skeleton has moved into a player's spot
				if next_space in [setup.player]:
					result = 3

				#Skeleton has moved into a hole
				elif next_space in [setup.hole]:

					#Adds the index to skkeletons being removed and returns it to a hole
					skeletons_removal.append(skel_number)
					board[new_position[0]][new_position[1]] = setup.hole

		skel_number += 1

	#Removes the skeleton from the list
	#Iterates in reverse so as not to cause problems
	for x in reversed(skeletons_removal):
		setup.skeleton_position.pop(x)

	return result

#Checks if the skeleton is next to the player, and will
#move into that square if that is the case
def check_adjacent_square(position,board):

	new_position = (-1,-1)

	if (board[position[0]-1][position[1]] == setup.player):
		new_position = (position[0]-1,position[1])
	elif (board[position[0]+1][position[1]] == setup.player):
		new_position = (position[0]+1,position[1])
	elif (board[position[0]][position[1]-1] == setup.player):
		new_position = (position[0],position[1]-1)
	elif (board[position[0]][position[1]+1] == setup.player):
		new_position = (position[0],position[1]+1)

	return new_position

#Determines where the next position happens to be
def process_move(action,position):

	new_position = (position[0],position[1])

	#Processes movement
	if action == "N":
		new_position = (position[0]-1,position[1])
	elif action == "S":
		new_position = (position[0]+1,position[1])
	elif action == "E":
		new_position = (position[0],position[1]+1)
	elif action == "W":
		new_position = (position[0],position[1]-1)

	return new_position

#Displays the end game result
def display_result(result,score,holes):

	response = ""

	if result == 1:
		response = "You're Free **\n"
		response = "Your performance rating is {}".format(int((60-score)/60*(96+holes)))
	elif result == 2:
		response = "You've fallen into one of your own holes"
	elif result == 3:
		response = "You've been scared to death by a skeleton"

	return response

#Resets the game if the player wishes to play again
def reset_game():

	setup.player_position = (2,2)
	setup.skeleton_position = [(4,18),(3,18),(2,18)]
	setup.hole_position = []

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Gravedigger",sys.modules[__name__])