# Creepy Computer Games

These files are a translation of an old programming book from the 1980s
called 'Creepy Computer Games'. The idea was to teach children programming
using basic. Due to multiple different systems back in the day there were marks
advising of when the code needed to be changed for a specific machine.

I used a Commodore 64 for my machine.

However, I have decided to translate them into modern computer languages. Initially
I was going to do it using C++, Java, and Python however issues arose that made me
decide to just use python, due to things that don't exist in modern langauges and would
require threading to be able to execute properly (though not necessarily in the same way
as it was executed on the older computers)

[The book is now available online to download for free](https://ia801902.us.archive.org/3/items/Creepy_Computer_Games_1983_Usborne_Publishing/Creepy_Computer_Games_1983_Usborne_Publishing.pdf)

## Executing the Games

A *shebang* has been included in the files so that they can be executed directly from the
command line. However, for that to work you will need to make the file executable. Since these
games run only on Linux, you will need to go to the directory on the command line and type

*chmod +x [game name].py*

However, a loader program has been included, so that is the only one that theoretically needs to be
executed as all of the other programs can be executed from that one.

## Issues

## Games

**Computer Nightmare**
This game simply involves copying a character that is displayed on the screen. You have three seconds
to press the correct key. Case is ignored where letters are concerned. If you are correct the score
increases, but if you are incorrect, or take to long, your score goes down. The game ends when you either
get more than 500 or less than 0.

**Number Wizard**
This game involves you matching the numbers that the wizard generates. You have numbers 1 to 9 available
but can only be used once, with the exception of 0, which can be used as many times as you like. The total of
the numbers you select must match the total of the numbers the wizard rolled. If you use all of you numbers you
win, but if you run out of turns, you lose. Oh, and if the wizard rolls a double, you get an extra turn.

**Ghost Guzzler**
This is sort of an arcade game where you have to match the number (that is the ghost). I have removed hard
coded numbers to make it easier to change the difficulty. The problem with the INKEY is also present, as you
need to press 'enter' after typing your action, otherwise nothing will happen. You can only increase the
number (though code to make it decrease isn't all that hard, and will probably make the game easier)

## Updates
**22 July 2023**
Created the initial folder to hold the contents on the game.
Added Computer Nightmare

**30 July 2023**
Added the Number Wizard Game
