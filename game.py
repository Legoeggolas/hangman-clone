"""
The main game loop.

Holds the GUI as well as the implementation of the game logic.
"""

from gamestate import GameState

import pygame
pygame.init()

# Set the window
screen = pygame.display.set_mode([500, 500])

# Run until the user clicks on  quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(400, 30, 90, 30))     
    pygame.display.flip() 