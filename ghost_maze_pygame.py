import pygame
from pygame.locals import *

def main():
    # Initialize Pygame
    pygame.init()

    # Set up display dimensions
    width, height = 850, 600
    screen = pygame.display.set_mode((width, height))

    # Set up the colors
    white = (255, 255, 255)


    # Main loop
    running = True
    while running:


        #First Squares
        pygame.draw.line(screen,white,(50,400),(300,400))
        pygame.draw.line(screen,white,(300,400),(550,400))
        pygame.draw.line(screen,white,(550,400),(800,400))
        pygame.draw.line(screen,white,(50,400),(50,150))
        pygame.draw.line(screen,white,(300,400),(300,150))
        pygame.draw.line(screen,white,(550,400),(550,150))
        pygame.draw.line(screen,white,(800,400),(800,150))
        pygame.draw.line(screen,white,(50,150),(300,150))
        pygame.draw.line(screen,white,(300,150),(550,150))
        pygame.draw.line(screen,white,(550,150),(800,150))

        #Second Squares
        pygame.draw.line(screen,white,(350,350),(500,350))


        pygame.display.flip()

def draw_square(screen,color,x,y,z):

    pygame.draw.line(screen,color,(x,z),(y,z))
    pygame.draw.line(screen,color,(x,z),(x,y))
    pygame.draw.line(screen,color,(x,y),(y,y))
    pygame.draw.line(screen,color,(y,y),(y,z))

main()

# Quit Pygame
pygame.quit()
