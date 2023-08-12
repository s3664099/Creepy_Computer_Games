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
instructions = "{}You might be lucky, she's in a good mood today. If you can guess the letter she is\n".format(instructions)
instructions = "{}thinking of, quickly enough, she will let you go free. if you, you'll probably get\n".format(instructions)
instructions = "{}turned into a fly.\n".format(instructions)
instructions = "{}To find the letter, give Spiderwoman a word and she will tell you whether or not\n".format(instructions)
instructions = "{}her letter is in it.\n".format(instructions)

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Starship Takeoff",sys.modules[__name__])