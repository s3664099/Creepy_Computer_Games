#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: Computer Nightmare
Author: Brendan Kayanagh
Translator: David Sarkies
Version: 0
Date: 22 July 2023
Source: https://ia801902.us.archive.org/3/items/Creepy_Computer_Games_1983_Usborne_Publishing/Creepy_Computer_Games_1983_Usborne_Publishing.pdf
This game can be found on page 3 of Creepy Computer Games, and it a python3 translation.

The goal of this game is to match the numbers that the computer throws at you. You get points for a correct
guess, and lose points for an incorrect guess. 

The computer will also throw insults at you as well (I'll stick with what they have).
"""

instructions = "You are a late-night computer addict and you've fallen asleep at the keyboard.\n"
instructions = "{}Suddenly your computer comes alive and starts hurling numbers and abuse at you.\n".format(instructions)
instructions = "{}To beat it you have to match the numbers as they appear on the screen. Your\n".format(instructions)
instructions = "{}starting score of 300 is increased if you hit the right number and descreased\n".format(instructions)
instructions = "{}if you don't. If you can get your score up to 500 the computer will give up and\n".format(instructions)
instructions = "{}you win, but if it goes down to zero, you will become a slave to your computer.\n".format(instructions)
instructions = "{}It's a real nightmare! Can you stay sane?\n".format(instructions)

#Array of insults that are thrown at the user
insults = ["** Micro's Rule **",
			"*People are stupid!*",
			"A Robot For President!",
			"Computers are great!",
			"*I'm better than you!*"]

#Stores the potential challenges
guess = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main_game():

	score = 300

	#Loop that continues while the score is within the win and lose
	while((score<500) and (score>0)):

		#Sets up the round
		util.clear_screen()
		number = randint(0,36)
		number = guess[number:number+1]

		print("\t\t{}\t\t{}".format(number,score))

		print_response(score)
		response = util.input_with_timeout_no_comment("",3)

		score -= 10

		#Was the guess correct, increases the score if it is
		if (response.upper() == str(number)):
			score += 10+(randint(0,15)*2)

	#Checks if it is a win or loss
	if score>500:
		print("Ok, you win, this time!")
	else:
		print("You're now my slave")

#If there is an insult, displays one based on the score
def print_insult(score):

	print(insults[int(score/100)])

#Checks if there is a response or an insult, and displays it
def print_response(score):

	if (randint(0,10)<5):
		print_insult(score)

	if(score<60):
		print("<There's No Hope>")
	elif (score>440):
		print("Urk! Help!")


#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Computer Nightmare",sys.modules[__name__])