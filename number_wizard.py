#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: 
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 0
Date: 20 October 2022
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 4 of Creepy Computer Games, and it a python3 translation.

"""

instructions = "This is the game the Number Wizard plays with all his visitors. He conjures the\n"
instructions = "{}numbers 1 to 9 in the air and then rolls two dice. You must give him two numbers\n".format(instructions)
instructions = "{}which both appear in the air and, when added together, give the same total and\n".format(instructions)
instructions = "{}the two numbers on the dice. Once you have used a number, its image disappears\n".format(instructions)
instructions = "{}from the air and you cannot use it again. You win if all the numbers have\n".format(instructions)
instructions = "{}disappeared before all your turns are used up. (you get an extra turn for every\n".format(instructions)
instructions = "{}double the wizard throws.) You are allowed to use zero as many times as you like\n".format(instructions)
instructions = "{}as one of your numbers. If you can't go, move on to the next turn by using two\n".format(instructions)
instructions = "{}zeros. See how many times you can beat the wizard".format(instructions)

def main_game():
	
	#Sets the array for the numbers
	number = []
	for x in range(10):
		number.append(x)

	#Sets the main variables, including the winner and same number flag
	numbers_used = 0
	turns = 8
	wizard_won = False
	same_number = False

	wizard_won = game_loop(number,numbers_used,turns,wizard_won,same_number)

	if (wizard_won == True):
		print("The wizard won")
	else:
		print("You won")

def game_loop(number,numbers_used,turns,wizard_won,same_number):

	while (numbers_used<8):

		util.clear_screen()

		if (same_number == True):
			print("You cannot use the same number other than 0 twice")

		same_number = False

		first_dice,second_dice = display(number,turns)

		if (first_dice == second_dice):
			turns += 2

		turns -= 1

		if (turns <= 0):
			wizard_won = True
			numbers_used = 10
		else:
			same_number = get_input(number,first_dice,second_dice)

	return wizard_won

def display(number,turns):

	number[0] = 1
	numbers_used = 0
	display_number = ""
	
	for x in range (0,10):

		if number[x] == 0:
			display_number+=" "
			numbers_used += 1
		else:
			display_number += "{}".format(x)

		display_number += " "

	print(display_number)
	print()
	print("You have {} turns left".format(turns))

	first_dice = randint(1,6)
	second_dice = randint(1,6)

	print("The dice throw is {}, {}".format(first_dice,second_dice))

	return first_dice,second_dice

def get_input(number,first_dice,second_dice):

	same_number = False

	first_choice = util.get_num_input("What is your first choice",0,9)
	second_choice = util.get_num_input("What is your second choice",0,9)

	if (first_choice+second_choice == first_dice+second_dice):
		if (((number[first_choice] != 0) and (number[second_choice] != 0)) and
			(first_choice != second_choice)):
			number[first_choice] = 0
			number[second_choice] = 0
		elif ((first_choice == second_choice) and (first_choice != 0)):
			same_number = True
	elif ((first_choice == second_choice) and (first_choice != 0)):
		same_number = True

	return same_number


#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Number Wizard",sys.modules[__name__])