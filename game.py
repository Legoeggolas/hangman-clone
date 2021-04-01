"""
The main game loop.

Holds the GUI as well as the implementation of the game logic.
"""

from gamestate import GameState

import pygame
pygame.init()

# Set the window
width=850
height=500


screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Hangman')
Font = pygame.font.Font('freesansbold.ttf', 25)


# Run until the user clicks on  quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        mx, my = pygame.mouse.get_pos()
        #button_1 = pygame.Rect(380, 200, 100, 25)

        s_diff=Font.render('Select difficulty', True, (0,255, 0))
        screen.blit(s_diff,(350,150))

        button_1=Font.render('Easy', True, (255,255, 0),(0, 0, 128))
        screen.blit(button_1,(180,200))

        button_2=Font.render('Medium', True, (255,255, 0),(0, 0, 128))
        screen.blit(button_2,(380,200))

        button_3=Font.render('Hard', True, (255,255, 0),(0, 0, 128))
        screen.blit(button_3,(600,200))

        '''
        if pygame.mouse.get_pressed()[0] and button_1.collidepoint((mx,my)):
            h_game()
        '''
        #pygame.draw.rect(screen,(0,0,255),button_1)

        Health = Font.render('Main Menu', True, (255, 0, 0))
        screen.blit(Health,((width//2)-50,50))
          
        pygame.display.update()


def h_game():
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        textsurface = Font.render('Health bar', False, (0, 128, 0))
        screen.blit(textsurface,(390,10))   
        pygame.display.flip() 