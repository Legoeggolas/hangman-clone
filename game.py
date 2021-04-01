"""
The main game loop.

Holds the GUI as well as the implementation of the game logic.
"""

from gamestate import GameState

import pygame
pygame.init()

# Set the window
screen = pygame.display.set_mode([500, 500])

health = pygame.font.Font('freesansbold.ttf', 20)

textsurface = health.render('Health bar', False, (0, 128, 0))

# Run until the user clicks on  quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(textsurface,(390,10))
    pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(400, 30, 90, 30))     
    pygame.display.flip() 