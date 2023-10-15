import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up display dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Define the square's properties
x, y = width // 2 - 50, height // 2 - 50  # Square's top-left corner coordinates
side_length = 100  # Length of each side of the square

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # Draw the square
    pygame.draw.rect(screen, white, (x, y, side_length, side_length))

    pygame.display.flip()

# Quit Pygame
pygame.quit()