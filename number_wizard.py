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
instructions = "{} numbers 1 to 9 in the air and then rolls two dice. You must give him two numbers\n".format(instructions)
instructions = "{} which both appear in the air and, when added together, give the same total and the two\n".format(instructions)
instructions = "{} numbers on the dice. Once you have used a number, its image disappears from the air\n".format(instructions)
instructions = "{} and you cannot use it again. You win if all the numebrs have disappeared before all\n".format(instructions)


#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Number Wizard",sys.modules[__name__])