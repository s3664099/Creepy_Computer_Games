#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: Spiderwoman
Author: Val Robinson
Translator: David Sarkies
Version: 0
Date: 12 August 2023
Source: https://ia601902.us.archive.org/3/items/Creepy_Computer_Games_1983_Usborne_Publishing/Creepy_Computer_Games_1983_Usborne_Publishing.pdf
This game can be found on page 8 of Computer Space Games, and it a python3 translation.

"""

instructions = "Eek! It's the Spiderwoman!\n"
instructions = "{}You might be lucky, she's in a good mood today. If you can guess the letter she\n".format(instructions)
instructions = "{}is thinking of, quickly enough, she will let you go free. if you, you'll\n".format(instructions)
instructions = "{}probably get turned into a fly.\n".format(instructions)
instructions = "{}To find the letter, give Spiderwoman a word and she will tell you whether or not\n".format(instructions)
instructions = "{}her letter is in it.\n".format(instructions)

letters = "abcdefghijklmnopqrstuvwxyz"

def main_game():

	util.clear_screen()

	#Select a random letter
	letter = randint(0,25)
	letter = letters[letter]
	tries = 0
	found_letter = False

	print("Spiderwoman has chosen\n\n")
	
	while (found_letter == False):
		word,tries = get_word(tries)

		#Checks if the letter is in the word
		if (check_word(word,letter) != -1):

			#It is, so a guess is offered (you only get one)
			print("It's one of those")
			print("\nWould you like to make a guess? (Y or N)")
			answer = util.yes_or_no(True)

			if (answer == True):
				found_letter = guess_letter(letter)

		else:
			print("It's not in that word")

#Processes guess and sees if it is the correct letter
def guess_letter(letter):

	guess = input("What is your guess then? ")

	if (guess.lower()[0] == letter):
		print("Ok - you can go")
		print("(This time)")
	else:
		print("You are too late")
		print("You are now a fly")

	return True

#Checks if the letter is in the word
def check_word(word,letter):

	return word.find(letter)

#Gets a word and returns it as lower case
def get_word(tries):

	correct_length = False

	while (correct_length == False):

		tries += 1

		word = input("Try a word: ")

		word_length = len(word)

		#Checks the length of the word
		if ((word_length>3) and (word_length<9)):
			correct_length = True
		elif (word_length<4):
			print("Word is too short\n")
		else:
			print("Word is too long\n")

	return word.lower(),tries




#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Starship Takeoff",sys.modules[__name__])