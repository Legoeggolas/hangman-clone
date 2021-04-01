"""
The main game loop.

Holds the GUI as well as the implementation of the game logic.
"""

from gamestate import GameState 

def easy():
    gs= GameState('EASY')
    running = True
    
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            screen.fill((0,0,0))
            if event.type == pygame.QUIT:
                screen.fill((0,0,0))
                pygame.quit()
                sys.exit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
        Hints = Font.render('Hints:', True, (0, 128, 0))
        
        screen.blit(Hints,(0,0))   
        gs.readyState()
        textsurface = Font.render('HP', True, (0, 128, 0))
        HP=Font.render(str(gs.healthPoints), True, (0, 128, 0))
        screen.blit(HP,(800,10))
        screen.blit(textsurface,(750,10))   
        pygame.display.flip() 


import pygame,sys
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
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    

        if event.type ==  pygame.MOUSEBUTTONDOWN:
            if 180 <= mouse[0] <= 180+65 and 200 <= mouse[1] <= 200+20:
                easy()
            
        screen.fill((0,0,0))
        mouse = pygame.mouse.get_pos()

        s_diff=Font.render('Select difficulty', True, (0,255, 0))
        screen.blit(s_diff,(350,150))

        button_1=Font.render('EASY', True, (255,255, 0),(0, 0, 128))
        screen.blit(button_1,(180,200))

        button_2=Font.render('MEDIUM', True, (255,255, 0),(0, 0, 128))
        screen.blit(button_2,(380,200))

        button_3=Font.render('HARD', True, (255,255, 0),(0, 0, 128))
        screen.blit(button_3,(600,200))

        
        
        menu = Font.render('Main Menu', True, (255, 0, 0))
        screen.blit(menu,((width//2)-50,50))
          
        pygame.display.update()


