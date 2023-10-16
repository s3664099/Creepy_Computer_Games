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


        #First Squares
        #pygame.draw.line(screen,white,(325,375),(500,375))
        #pygame.draw.line(screen,white,(325,375),(325,200))
        
        #Second Squares
        #pygame.draw.line(screen,white,(350,350),(475,350))
        #pygame.draw.line(screen,white,(350,350),(350,225))
        #pygame.draw.line(screen,white,(350,225),(475,225))
        #pygame.draw.line(screen,white,(475,225),(475,350))

        #Third Squares
        #pygame.draw.line(screen,white,(375,325),(450,325))
        #pygame.draw.line(screen,white,(375,325),(375,250))
        #pygame.draw.line(screen,white,(375,250),(450,250))
        #pygame.draw.line(screen,white,(450,250),(450,325))

        #Fourth Squares
        pygame.draw.line(screen,white,(400,300),(425,300))
        pygame.draw.line(screen,white,(400,300),(400,275))
        pygame.draw.line(screen,white,(400,275),(425,275))
        pygame.draw.line(screen,white,(425,275),(425,300))

        pygame.display.flip()

def draw_square(screen,color,x,y,z):

    pygame.draw.line(screen,color,(x,z),(y,z))
    pygame.draw.line(screen,color,(x,z),(x,y))
    pygame.draw.line(screen,color,(x,y),(y,y))
    pygame.draw.line(screen,color,(y,y),(y,z))

display_grid = [['#','#','#'],['#','#','#'],['#','#','#']]

main()

# Quit Pygame
pygame.quit()
