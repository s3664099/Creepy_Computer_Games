"""
Title: Ghost Maze Pygame Function
Version: 0.8
Date: 23 October 2023
"""

import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()


# Set up the colors
white = (255, 255, 255)
red = (255,0,0)

def create_screen():

    # Set up display dimensions
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))

    return screen

def display(display_grid,screen):

    # Main loop
    running = True
    while running:

        x_pos_start = 375
        y_pos_start = 300
        size = 20
        size_start = 0

        #Moves through the grid
        for x in display_grid:

            x_position = x_pos_start
            y_position = y_pos_start
            pos = 0

            for y in x:


                #Checks whether there is an exit, and if so changes the colour to red
                colour = white

                if y =="X":
                    colour = red
                    y = "#" 

                polygon_size = size/2

                #Checks whether there is a wall
                if y == "#":

                    #Checks which position the wall is on, and then draws the appropriate polygon
                    if pos == 0:

                        if size_start == 0:
                            pygame.draw.polygon(screen,colour, ((x_position,y_position),(x_position+size,y_position),(x_position+size+polygon_size,y_position+polygon_size),(x_position+size,y_position+size),(x_position,y_position+size)))
                        else:
                            pygame.draw.polygon(screen,colour, ((x_position,y_position),(x_position+size,y_position),(x_position+size+(polygon_size/2),y_position+(polygon_size/2)),
                                                (x_position+size+(polygon_size/2),y_position+(size/2+polygon_size/2)),(x_position+size,y_position+size),(x_position,y_position+size)))

                    if pos == 1:
                        pygame.draw.rect(screen,colour,(x_position,y_position,size,size)) 

                    if pos == 2:

                        if size_start == 0:
                            pygame.draw.polygon(screen,colour, ((x_position,y_position),(x_position-polygon_size,y_position+polygon_size),(x_position,y_position+size),(x_position+size,y_position+size),(x_position+size,y_position)))
                        else:
                            pygame.draw.polygon(screen,colour, ((x_position,y_position),(x_position-(polygon_size/2),y_position+(polygon_size/2)),(x_position-(polygon_size/2),y_position+(size/2+polygon_size/2)),(x_position,y_position+size),
                                                (x_position+size,y_position+size),(x_position+size,y_position)))

                pos+=1

                x_position += size

            x_pos_start = x_pos_start - (size * 2) + (size/2)
            y_pos_start = y_pos_start - (size/2)
            size *=2
            size_start +=1

        pygame.display.flip()

display_grid = [['','',''],['#','','#'],['','','']]

screen = create_screen()
display(display_grid, screen)

# Quit Pygame
pygame.quit()
