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
            pygame.draw.rect(screen, white, (375,300,20,20))
            pygame.draw.polygon(screen,white,((395,300),(405,310),(395,320)))
        if (display_grid[0][1] == "#"):
            pygame.draw.rect(screen, white, (395,300,20,20))
        if (display_grid[0][2] == "#"):
            pygame.draw.rect(screen, white, (415,300,20,20))
            pygame.draw.polygon(screen, white, ((415,300),(405,310),(415,320)))
        if (display_grid[1][0] == "#"):
            pygame.draw.rect(screen,white, (345,290,40,40))
            pygame.draw.polygon(screen,white,((385,290),(395,300),(395,320),(385,330)))
        if (display_grid[1][1] == "#"):
            pygame.draw.rect(screen,white, (385,290,40,40))
        if (display_grid[1][2] == "#"):
            pygame.draw.rect(screen,white, (425,290,40,40))
            pygame.draw.polygon(screen,white, ((425,290),(415,300),(415,320),(425,330)))
        if (display_grid[2][0] == "#"):
            pygame.draw.rect(screen,white, (285,270,80,80))
            pygame.draw.polygon(screen,white, ((365,270),(385,290),(385,330),(365,350)))           
        if (display_grid[2][1] == "#"):
            pygame.draw.rect(screen,white, (365,270,80,80))
        if (display_grid[2][2] == "#"):
            pygame.draw.rect(screen,white, (445,270,80,80))
            pygame.draw.polygon(screen,white, ((445,270),(425,290),(425,330),(445,350)))

        pygame.display.flip()

def draw_square(screen,color,x,y,z):

    pygame.draw.line(screen,color,(x,z),(y,z))
    pygame.draw.line(screen,color,(x,z),(x,y))
    pygame.draw.line(screen,color,(x,y),(y,y))
    pygame.draw.line(screen,color,(y,y),(y,z))

display_grid = [['#','','#'],['#','','#'],['#','','#']]

main(display_grid)

# Quit Pygame
pygame.quit()
