#!/usr/bin/env python3

import loader
import sys
import util
import time
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

characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def title(score,guesses):
	spaces = util.tab(8,4)
	util.clear_screen()
	print("{}Sceance".format(spaces))
	print("\nscore: {}   guesses: {}\n\n".format(score,guesses))

#Constucts the dictionary to hold the position of a letter
def set_position(x,y,letter):

	return {"x": x, "y": y,"Letter": letter}

#Constructs the list for the letters' positions
def build_positions_list():

	positions = []

	for i in range(8):

		positions.append(set_position(5,6+i,characters[i]))
		positions.append(set_position(11,6+i,characters[20-i]))

	for i in range(5):

		positions.append(set_position(6+i,5,characters[25-i]))
		positions.append(set_position(6+i,14,characters[8+i]))

	return positions

#Builds the main screen
def build_screen(positions):

	display = print_padding("")

	#Builds the lines
	for x in range(14):

		#Checks to see if there are letters on the lines
		row_found = False

		for position in positions:

			#There is a letter on the line
			if position["x"] == x:

				#Flags that a letter is on the line
				row_found = True

				#Builds padding
				for y in range(10):
					display += " "

				for y in range(18):

					#Checks if there are letters at the position
					letter_present = False
					for h_position in positions:

						#Looks for letters
						if h_position["y"] == y and h_position['x'] == x:

							#Flags that there is a letter
							display += h_position['Letter']
							letter_present = True
					
					if letter_present == False:
						display += " "

				#Creates a line break and breaks			
				display += "\n"
				break

		#Otherwise a blank line is printed
		if row_found == False:
			display = get_blank_line(display)+"\n"

	print(display)

#Prints padding at the top
def print_padding(display):

	for x in range(3):
		display = get_blank_line(display)
		display += "\n"

	return display

#The line is blank
def get_blank_line(display):

	for y in range(80):
		display += " "
	return display

def position_star(positions,letters):

	star = "*"
	rand_letter = randint(0,25)
	letter = characters[rand_letter]

	y=4
	x=31-rand_letter

	if rand_letter<21:
		x=12
		y=26-rand_letter
	if rand_letter<13:
		y=15
		x=rand_letter-2
	if rand_letter<8:
		x=4
		y=rand_letter+6

	positions.append(set_position(x,y,star))
	letters+=letter

	return positions,letters

def guess_word(word,score):

	correct = False
	guesses = 0
	print("Word {}: ".format(word))
	while (not correct):
		guess = input("What is your guess: ")

		if guess == word:
			score += len(word)
			correct = True
		else:
			guesses += 1

			if guesses == 1:
				print("The table begins to shake.")
			elif guesses == 2:
				print("The light build shatters")
			elif guesses == 3:
				print("A pair of clammy hands grasps your neck")
				correct = True

	return score,guesses

#Sets the difficulty for the game
def get_difficulty():

	difficulty = util.get_num_input("What Difficulty Would You Like (1 Easy, 5 Impossible)",1,5)
	speed = 0
	word_size = 0
	score_goal = 0

	if difficulty == 1:
		speed = 5
		word_size = randint(1,3)
		score_goal = 10
	elif difficulty == 2:
		speed = 4
		word_size = randint(2,5)
		score_goal = 20
	elif difficulty == 3:
		speed = 3
		word_size = randint(3,7)
		score_goal = 30
	elif difficulty == 4:
		speed = 2
		word_size = randint(5,10)
		score_goal = 40
	else:
		speed = 1
		word_size = randint(10,20)
		score_goal = 50

	return speed,word_size,score_goal

def main_game():

	speed,word_size,score_goal = get_difficulty()
	score = 0
	guesses = 0
	game_end = False

	#Main Loop
	while (game_end == False):

		letters = ""

		#Turn Loop
		for x in range(word_size):
			title(score,guesses)
			positions = build_positions_list()
			positions,letters = position_star(positions,letters)
			build_screen(positions)
			time.sleep(speed)

		title(score,guesses)
		score, guesses = guess_word(letters,score)

		if (guesses == 3):
			game_end = True
		elif (score>=score_goal):
			game_end = True

	if (guesses == 3):
		print("Too bad, you lose")
	else:
		print("Congratulations, you won")

		#Difficulty Level - Increase speed, number of letters
		#Create an easy, medium, hard, difficult, impossible options (longer word, faster times)
		#Add library of words and phrases.

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Scence",sys.modules[__name__])