"""
Title: Graphics Package
Translator: David Sarkies
Version: 1
Date: 8 October 2022

This file holds a series of functions that enable graphical displays using pygame.

To install pygame you need to do the following:

pip3 install pygame
"""

import pygame

#Initialises the PyGame library and creates the window with the caption being the title of the game
pygame.init()

#Sets up the display dimensions
cell_size = 50
columns = 20
rows = 10
display_width = cell_size * columns
display_height = cell_size * rows
player = pygame.transform.scale(pygame.image.load("icons/worker.png"),(cell_size,cell_size))
wall = pygame.transform.scale(pygame.image.load("icons/wall.png"),(cell_size,cell_size))
skeleton = pygame.transform.scale(pygame.image.load("icons/skeleton.png"),(cell_size,cell_size))
stone = pygame.transform.scale(pygame.image.load("icons/gravestone.png"),(cell_size,cell_size))
hole = pygame.transform.scale(pygame.image.load("icons/hole.png"),(cell_size,cell_size))

def display_screen():
	gameDisplay = pygame.display.set_mode((display_width,display_height))
	return gameDisplay

#Sets the caption of the screen
def set_caption(title):
	pygame.display.set_caption(title)

def update_screen(display,board):

	# Clear the screen
	display.fill((0, 0, 0))

	#Go through the board
	for col in range(columns):
		for row in range(rows):

			if board[row][col] == "*":
				display.blit(player, (col * cell_size, row * cell_size))
			elif board[row][col] == "+":
				display.blit(stone, (col * cell_size, row * cell_size))
			elif board[row][col] == "O":
				display.blit(hole, (col * cell_size, row * cell_size))
			elif board[row][col] == "X":
				display.blit(skeleton, (col * cell_size, row * cell_size))
			elif board[row][col] == ":":
				display.blit(wall, (col * cell_size, row * cell_size))

	pygame.display.update()

def get_keypress():

	events = pygame.event.get()
	key = ""

	for event in events:
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP or event.key == pygame.K_n:
				key = "N"
			elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
				key = "S"
			elif event.key == pygame.K_LEFT or event.key == pygame.K_w:
				key = "W"
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_e:
				key = "E"
			elif event.key == pygame.K_q:
				key = "Q"
			elif event.key == event.key == pygame.K_d:
				key = "D"
			elif event.key == pygame.K_SPACE or event.key == pygame.K_x:
				key = "X"			

	return key

"""
Skeleton - https://www.flaticon.com/free-icons/skeleton Skeleton icons created by Freepik - Flaticon
Gravestone - https://www.flaticon.com/free-icons/death Death icons created by Eucalyp - Flaticon
Wall - https://www.flaticon.com/free-icons/brick Brick icons created by Ehtisham Abid - Flaticon
Hole - https://www.flaticon.com/free-icons/hole Hole icons created by Freepik - Flaticon
Player - https://www.flaticon.com/free-icons/worker Worker icons created by Backwoods - Flaticon
"""