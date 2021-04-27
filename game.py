"""
The main game loop.

Holds the GUI as well as the implementation of the game logic.
"""

from gamestate import GameState 
import pygame,sys

def main():
    pygame.init()

    # The game window's attributes and other PyGame specific settings
    SCREEN_WIDTH = 850
    SCREEN_HEIGHT = 500
    FONT_SIZE = 25
    HINTFONT_SIZE = 15

    clk=pygame.time.Clock()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption('Hangman')
    Font = pygame.font.SysFont('Verdana', FONT_SIZE)
    hfont = pygame.font.SysFont('Verdana', HINTFONT_SIZE)


    # The function that holds the game loop
    def game(gamediff: str):

        # Initialization of the game state
        gs = GameState(gamediff)
        gs.getNextWord()
        

        # The actual game loop
        while True:
            screen.fill((0, 0, 0))   

            if gs.healthPoints <= 0:        # End the game if the number of tries goes down to zero, loss condition
                promptText = Font.render("Sorry, but you are all out of tries!", True, (255, 0, 0))
                screen.blit(promptText, promptText.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            elif not gs.currWord:           # End the game if the wordList gets exhausted, win condition
                promptText = Font.render("Congratulations, you have correctly guessed all of the words!", True, (255, 0, 0))
                screen.blit(promptText, promptText.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            else:
                # Render the remaining tries
                hpPrompt = Font.render("Tries: " + str(gs.healthPoints), True, (0, 128, 0))
                screen.blit(hpPrompt, hpPrompt.get_rect(center = (18*SCREEN_WIDTH/20, SCREEN_HEIGHT/20)))

                # Render the word being guessed
                word=Font.render(gs.currWord.getDashedWord(), True, (0, 0, 255))
                screen.blit(word, word.get_rect(center = (SCREEN_WIDTH/2, 3*SCREEN_HEIGHT/4)))

                # Render hints based on the difficulty setting
                hint_max = 3 - ["EASY", "MEDIUM", "HARD"].index(gs.difficulty)
                hintPrompt = Font.render('Hints:', True, (0, 128, 0))
                screen.blit(hintPrompt, hintPrompt.get_rect(center = (SCREEN_WIDTH/20, SCREEN_HEIGHT/20)))  
                for index in range(min(hint_max, len(gs.currWord.clueList))):
                    thisHint = hfont.render(gs.currWord.clueList[index], True, (0, 128, 0))
                    screen.blit(thisHint, (SCREEN_WIDTH/20, 45 + index*15))    
                
                # Render the instructions
                instructorPrompt = hfont.render('Enter the character you want to fill the leftmost blank with', True, (0, 255, 0))
                screen.blit(instructorPrompt, instructorPrompt.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/3)))

                # Evaluate the Event queue
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()   

                    # Check whether an alphabet key was pressed
                    if event.type == pygame.KEYDOWN:
                        if event.key >= 97 and event.key <= 122:
                            charPlaceEvent = gs.currWord.placeChar(chr(event.key).upper())
                            if charPlaceEvent == True:
                                screen.fill((0, 0, 0))
                                promptText = hfont.render('You guessed correctly!', True, (0, 255, 0))
                                screen.blit(promptText, promptText.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4)))
                            else:
                                screen.fill((0, 0, 0))
                                promptText = hfont.render('You guessed the wrong letter!', True, (255, 0, 0))
                                screen.blit(promptText, promptText.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4)))
                                gs.healthPoints -= 1
                    
                    # If the word was finished, stop listening for events and quit
                    if gs.currWord.isFinished():
                        print("Word finished: " + gs.currWord.finishedWord)
                        gs.getNextWord()
                        break
            
            # Display the rendered frame
            pygame.display.flip()
            clk.tick(3)        # Limit the frames to 6


    # The main menu
    running = True
    while running:
        screen.fill((0 ,0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        
            # Checks if the area of mouse press corresponds to any of the options
            if event.type ==  pygame.MOUSEBUTTONDOWN:
                # The "EASY" difficulty option
                if SCREEN_WIDTH/4-125 <= mouse[0] <= SCREEN_WIDTH/4+125 and SCREEN_HEIGHT/2-FONT_SIZE <= mouse[1] <= SCREEN_HEIGHT/2+FONT_SIZE:
                    game("EASY")
                # The "MEDIUM" difficulty option
                elif SCREEN_WIDTH/2-125 <= mouse[0] <= SCREEN_WIDTH/2+125 and SCREEN_HEIGHT/2-FONT_SIZE <= mouse[1] <= SCREEN_HEIGHT/2+FONT_SIZE:
                    game("MEDIUM")
                # The "HARD" difficulty option
                elif 3*SCREEN_WIDTH/4-125 <= mouse[0] <= 3*SCREEN_WIDTH/4+125 and SCREEN_HEIGHT/2-FONT_SIZE <= mouse[1] <= SCREEN_HEIGHT/2+FONT_SIZE:
                    game("HARD")              
                
            mouse = pygame.mouse.get_pos()

            s_diff=Font.render('Select difficulty', True, (0, 255, 0))
            screen.blit(s_diff,s_diff.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/3)))

            # Draw each of the difficulty options
            button_1=Font.render('EASY', True, (255,255, 0), (0, 0, 128))
            screen.blit(button_1, button_1.get_rect(center=(SCREEN_WIDTH/4, SCREEN_HEIGHT/2)))

            button_2=Font.render('MEDIUM', True, (255,255, 0), (0, 0, 128))
            screen.blit(button_2, button_2.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)))

            button_3=Font.render('HARD', True, (255,255, 0), (0, 0, 128))
            screen.blit(button_3, button_3.get_rect(center=(3*SCREEN_WIDTH/4, SCREEN_HEIGHT/2)))

            menu = Font.render('Main Menu', True, (255, 0, 0))
            screen.blit(menu, menu.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/6)))  
            pygame.display.update()
            clk.tick(30)

if __name__ == "__main__":
    main()