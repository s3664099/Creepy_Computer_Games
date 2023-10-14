#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: Ghost Maze
Author: Colin Reynolds
Translator: David Sarkies
Version: 0
Date: 29 September 2023
Source: https://ia601902.us.archive.org/3/items/Creepy_Computer_Games_1983_Usborne_Publishing/Creepy_Computer_Games_1983_Usborne_Publishing.pdf
This game can be found on page 14 of Creepy Computer Games, and it a python3 translation.

"""

instructions = "It's a creepy sort of place. The identical dark corridors don't seem to go\n"
instructions = "{}anywhere. It might even be haunted. You can only see straight in front of you,\n".format(instructions)
instructions = "{}and you can only move in the direction in which you are facing. You can turn\n".format(instructions)
instructions = "{}left or right, but this won't actually move you anywhere, it will just show you\n".format(instructions)
instructions = "{}another view. All you have to do is find the cross which marks the way out. Your\n".format(instructions)
instructions = "{}position is marked with a Y and walls are marked #\n".format(instructions)
instructions = "{}Gulp! It is haunted. Ghosts are shown by the letter G. If you get right up next\n".format(instructions)
instructions = "{}to one you will be whisked away to another part of the maze, not knowing where\n".format(instructions)
instructions = "{}you are on in which direction you are facing. Here are the keys you can use:\n".format(instructions)
instructions = "{}X: Moves you forward\n".format(instructions)
instructions = "{}N: Turns you left (through 90 degrees)\n".format(instructions)
instructions = "{}M: Turns you right (through 90 degrees)\n".format(instructions)

def main_game():

	#Set up the game
	maze_width = 10
	maze_height = 7
	maze_array = build_maze([])
	ghost_move = -1
	move = 0
	ghosts_pos = position_ghost(maze_array,0)
	ghost_move += 1
	player_location = place_player(maze_array)
	player_facing = randint(0,4)

	playing = True

	while (playing):

		print(player_location)
		print(ghosts_pos)

		#Checks if player is next to a ghost
		if(check_position(ghosts_pos,player_location,maze_width)):
			player_location = place_player(maze_array)
			ghosts_pos = position_ghost(maze_array,ghosts_pos)
			move = 0
			ghost_move += 1

		#Checks if it is time for the ghost to move
		if (move == 5):
			ghosts_pos = position_ghost(maze_array,ghosts_pos)
			move = 0
			ghost_move += 1		

		display_position(player_facing,maze_array,player_location,maze_width)

		action = get_input()

		if (action.lower() == "q"):
			playing = False
		elif ((action.lower()=="m") or (action.lower()=="n")):
			player_facing = change_facing(action.lower(),player_facing)
		elif (action.lower() == "x"):
			if ((player_facing == 0) and (maze_array[player_location-10] != 0)):
				player_location -=10
			elif ((player_facing == 2) and (maze_array[player_location+10] !=0)):
				player_location += 10
			elif ((player_facing == 1) and (maze_array[player_location+1] !=0)):
				player_location += 1
			elif ((player_facing == 3) and (maze_array[player_location-1] !=0)):
				player_location -= 1
			else:
				print("You cannot go there")

		if (maze_array[player_location] == 9):
			print("You have escaped in {} moves".format(ghost_move*5+move))
			playing = False

		move += 1

#Changes the player's facing
def change_facing(action, player_facing):

	#Turn Left?
	if (action == "m"):
		player_facing += 1

		if (player_facing == 4):
			player_facing = 0

	#Turn right
	elif (action == "n"):
		player_facing -= 1

		if (player_facing == -1):
			player_facing = 3

	return player_facing

def display_position(facing,maze_array,player_location,width):

	display_grid = []

	for x in range(3):

		grid_row = []
		spot = x-1

		if (facing == 0):
			grid_row.append(player_location-width*spot+1)
			grid_row.append(player_location-width*spot)
			grid_row.append(player_location-width*spot-1)
		elif (facing == 1):
			grid_row.append(player_location+width+spot)
			grid_row.append(player_location+spot)
			grid_row.append(player_location-width+spot)
		elif (facing == 2):
			grid_row.append(player_location+width*spot-1)
			grid_row.append(player_location+width*spot)
			grid_row.append(player_location+width*spot+1)
		else:
			grid_row.append(player_location-spot-width)
			grid_row.append(player_location-spot)
			grid_row.append(player_location-spot+width)

		display = []	

		for y in range(3):

			if maze_array[grid_row[y]] == 0:
				display.append("#")
			elif maze_array[grid_row[y]] == 1:
				display.append(".")
			elif maze_array[grid_row[y]] == 2:
				display.append("G")
			else:
				display.append("X")

		display_grid.append(display)
	display_grid[1][1] = "Y"

	for x in range(3):
		view = ""
		for y in range(3):
			view = "{}{}".format(view,display_grid[x][y])
		print(view)

#Builds the maze
def build_maze(maze_array):

	maze = ""
	maze = "{}0000000000".format(maze)
	maze = "{}0111100110".format(maze)
	maze = "{}0010011100".format(maze)
	maze = "{}0011010110".format(maze)
	maze = "{}0110100100".format(maze)
	maze = "{}0011111100".format(maze)
	maze = "{}0000009000".format(maze)

	for x in maze:
		maze_array.append(int(x))

	return maze_array

#Gets player input
def get_input():

	correct = False
	action = ""

	#Checks if valid action
	while(not correct):

		action = input()
		if ((action.lower() == "m") or (action.lower() == "n") or (action.lower() == "x") or (action.lower() == "q")):
			correct = True

	return action


#Positions the player on the map
def place_player(maze_array):

	player_location = 0

	#Checks that the position is not a wall
	while (maze_array[player_location] == 0):
		player_location = randint(0,len(maze_array))

	return player_location

#Moves the ghost
def position_ghost(maze_array,ghosts_pos):

	#Returns the ghost position to a space
	if maze_array[ghosts_pos] == 2:
		maze_array[ghosts_pos] = 1

	#Checks that the ghost is not in a wall
	while (maze_array[ghosts_pos] == 0):
		ghosts_pos = randint(0,len(maze_array-1))

	maze_array[ghosts_pos] = 2

	return ghosts_pos

#Checks if the player is next to the ghost
def check_position(ghost,player,width):

	position = False

	if ((player+width == ghost) or (player-width == ghost)
		or (player+1 == ghost) or (player-1 == ghost)):
		position = True

	return position

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Starship Takeoff",sys.modules[__name__])