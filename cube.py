import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up display dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Define cube vertices
vertices = [
    (100, 100, 100),
    (200, 100, 100),
    (200, 200, 100),
    (100, 200, 100),
    (100, 100, 200),
    (200, 100, 200),
    (200, 200, 200),
    (100, 200, 200)
]

# Define cube edges by connecting vertices
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # Project 3D vertices onto 2D
    projected_vertices = []
    for vertex in vertices:
        x, y, z = vertex
        f = 200 / (200 + z)  # Perspective projection
        projected_x = x * f + width / 2
        projected_y = y * f + height / 2
        projected_vertices.append((projected_x, projected_y))

    # Draw the cube edges
    for edge in edges:
        start, end = edge
        pygame.draw.line(screen, white, projected_vertices[start], projected_vertices[end])

    pygame.display.flip()

# Quit Pygame
pygame.quit()
