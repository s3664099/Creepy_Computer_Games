#!/usr/bin/env python3

import loader
import sys
import util
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

instructions = "It's dark and windy - not the kind of night to be lost in a\n"
instructions = "{}graveyard, but that's where you are. You have until midnight\n".format(instructions)
instructions = "{}to find your way out. Skeletons lurk in the shadows waiting\n".format(instructions)

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Starship Takeoff",sys.modules[__name__])