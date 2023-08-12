#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: 
Author: 
Translator: David Sarkies
Version: 0
Date: 
Source: https://ia601902.us.archive.org/3/items/Creepy_Computer_Games_1983_Usborne_Publishing/Creepy_Computer_Games_1983_Usborne_Publishing.pdf
This game can be found on page {} of Creepy Computer Games, and it a python3 translation.

"""

instructions = ""

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Starship Takeoff",sys.modules[__name__])