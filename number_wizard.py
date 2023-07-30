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
	
	number = []

	for x in range(10):
		number.append(x)

	numbers_used = 0
	turns = 8
	wizard_won = False

	while (numbers_used<9):

		util.clear_screen()
		display_number = ""
		number[1] = 1

		for x in range (1,10):

			if number[x] == 0:
				display_number+=" "
				numbers_used += 1
			else:
				display_number += "{}".format(x-1)

			display_number += " "

		print(display_number)
		print()
		print("You have {} turns left".format(turns))

		first_dice = randint(1,6)
		second_dice = randint(1,6)

		print("The dice throw is {}, {}".format(first_dice,second_dice))

		if (first_dice == second_dice):
			turns += 2

		turns -= 1

		if (turns <= 0):
			wizard_won = True
		else:
			first_choice = util.get_num_input("What is your first choice",0,9)
			second_choice = util.get_num_input("What is your second choice",0,9)

		if ((first_choice+second_choice == first_dice+second_dice) or (number[first_choice+1] != 0)
			or (number[second_choice+1] != 0)):
			number[first_choice+1] = 0
			number[second_choice+1] = 0

	if (wizard_won == True):
		print("The wizard won")
	else:
		print("You won")

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Number Wizard",sys.modules[__name__])