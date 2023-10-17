import pygame
from pygame.locals import *

def main(display_grid):
    # Initialize Pygame
    pygame.init()

    # Set up display dimensions
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))

    # Set up the colors
    white = (255, 255, 255)


    # Main loop
    running = True
    while running:

        if (display_grid[0][0] == "#"):
            pygame.draw.rect(screen, white, (375,300,25,25))
        if (display_grid[0][1] == "#"):
            pygame.draw.rect(screen, white, (400,300,25,25))
        if (display_grid[0][2] == "#"):
            pygame.draw.rect(screen, white, (425,300,25,25))

        pygame.display.flip()

def draw_square(screen,color,x,y,z):

    pygame.draw.line(screen,color,(x,z),(y,z))
    pygame.draw.line(screen,color,(x,z),(x,y))
    pygame.draw.line(screen,color,(x,y),(y,y))
    pygame.draw.line(screen,color,(y,y),(y,z))

display_grid = [['#','','#'],['#','#','#'],['#','#','#']]

main(display_grid)

# Quit Pygame
pygame.quit()
