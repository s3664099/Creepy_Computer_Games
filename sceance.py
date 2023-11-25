#!/usr/bin/env python3

import loader
import sys
import util
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

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Starship Takeoff",sys.modules[__name__])