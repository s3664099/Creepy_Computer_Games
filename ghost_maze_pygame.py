import pygame
from pygame.locals import *

def main():
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
        
        #Second Squares
        #pygame.draw.line(screen,white,(325,375),(525,375))

        #Third Squares
        #pygame.draw.line(screen,white,(350,350),(500,350))

        #Fourth Squares
        pygame.draw.line(screen,white,(400,300),(450,300))
        pygame.draw.line(screen,white,(400,300),(400,250))
        pygame.draw.line(screen,white,(400,250),(450,250))
        pygame.draw.line(screen,white,(450,250),(450,300))

        pygame.display.flip()

def draw_square(screen,color,x,y,z):

    pygame.draw.line(screen,color,(x,z),(y,z))
    pygame.draw.line(screen,color,(x,z),(x,y))
    pygame.draw.line(screen,color,(x,y),(y,y))
    pygame.draw.line(screen,color,(y,y),(y,z))

main()

# Quit Pygame
pygame.quit()
