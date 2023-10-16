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

# Set the dot spacing
spacing = 50

# Define the font for numbering
font = pygame.font.Font(None, 36)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # Draw dots and numbers
    for x in range(0, width, spacing):
        for y in range(0, height, spacing):
            # Draw a dot
            pygame.draw.circle(screen, white, (x, y), 3)

            # Draw column and row numbers
            if x == 0:
                text = font.render(str(y // spacing), True, white)
                screen.blit(text, (5, y - 18))
            if y == 0:
                text = font.render(str(x // spacing), True, white)
                screen.blit(text, (x + 5, 5))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
