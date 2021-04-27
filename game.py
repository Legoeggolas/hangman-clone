"""
The main game loop.

Holds the GUI as well as the implementation of the game logic.
"""

from gamestate import GameState 
import pygame,sys

pygame.init()

# Set the window
width=850
height=500

clk=pygame.time.Clock()
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Hangman')
Font = pygame.font.Font('freesansbold.ttf', 25)
hfont = pygame.font.Font('freesansbold.ttf', 15)

def game(gamediff: str):
    gs = GameState(gamediff)

    running = True
    while running:
        screen.fill((0,0,0))
                    
        Hints = Font.render('Hints:', True, (0, 128, 0))
        
        screen.blit(Hints,(0,0))   
        
        HP=Font.render(str(gs.healthPoints), True, (0, 128, 0))
        screen.blit(HP,(800,10))
        
         
        pygame.display.flip()
        clk.tick(30) 
        

        gs.getNextWord()
        # implementation of game hangman
        while gs.healthPoints!=0 or (gs.currWord!='None') :
            while gs.healthPoints!=0 or gs.currWord.isFinished()=='False' :
                
                textsurface = Font.render('HP', True, (0, 128, 0))
                screen.blit(textsurface,(750,10))
                HP=Font.render(str(gs.healthPoints), True, (0, 128, 0))
                screen.blit(HP,(800,10))

                word=Font.render(gs.currWord.dashedWord, True, (0,0, 255))
                screen.blit(word, (250,300))

                if gamediff=='EASY':
                    hint_max=3
               
                if gamediff=='MEDIUM':
                    hint_max=2
                    
                if gamediff=='HARD':
                    hint_max=1

                len_clue=len(gs.currWord.clueList)
                screen.blit(Hints,(0,0))
                x=0
                y=30
                for i in range(len_clue):
                    if hint_max<i:
                        break
                    Hts=hfont.render(gs.currWord.clueList[i], True, (0, 128, 0))
                    screen.blit(Hts,(x,y))
                    y=y+15    
                
                instruct=hfont.render('Enter character to the guess the word from left to right', True, (0, 255, 0))
                screen.blit(instruct,(200,200))
                
                
                for event in pygame.event.get():
                    # Did the user click the window close button?
                    if event.type == pygame.QUIT:
                        
                        pygame.quit()
                        sys.exit()
                        running = False    
                    if event.type== pygame.KEYDOWN:
                        if event.key==pygame.K_a:
                            if gs.currWord.placeChar('A')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                                
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1
                        
                        if event.key==pygame.K_b:
                            if gs.currWord.placeChar('B')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_c:
                            if gs.currWord.placeChar('C')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_d:
                            if gs.currWord.placeChar('D')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1
                        
                        if event.key==pygame.K_e:
                            if gs.currWord.placeChar('E')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_f:
                            if gs.currWord.placeChar('F')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_g:
                            if gs.currWord.placeChar('G')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1        

                        if event.key==pygame.K_h:
                            if gs.currWord.placeChar('H')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_i:
                            if gs.currWord.placeChar('I')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_j:
                            if gs.currWord.placeChar('J')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_k:
                            if gs.currWord.placeChar('K')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_l:
                            if gs.currWord.placeChar('L')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_m:
                            if gs.currWord.placeChar('M')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_n:
                            if gs.currWord.placeChar('N')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_o:
                            if gs.currWord.placeChar('O')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_p:
                            if gs.currWord.placeChar('P')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_q:
                            if gs.currWord.placeChar('Q')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_r:
                            if gs.currWord.placeChar('R')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_s:
                            if gs.currWord.placeChar('S')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_t:
                            if gs.currWord.placeChar('T')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_u:
                            if gs.currWord.placeChar('U')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_v:
                            if gs.currWord.placeChar('V')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_w:
                            if gs.currWord.placeChar('W')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_x:
                            if gs.currWord.placeChar('X')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_y:
                            if gs.currWord.placeChar('Y')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                        if event.key==pygame.K_z:
                            if gs.currWord.placeChar('Z')=='True':
                                screen.fill((0,0,0))
                                yay=hfont.render('Correct , You got the correct letter', True, (0, 255, 0))
                                screen.blit(yay,(200,100))
                    
                            else:
                                screen.fill((0,0,0))
                                nay=hfont.render('Wrong Letter, Keep Guessing', True, (255, 0, 0))
                                screen.blit(nay,(200,100))
                                gs.healthPoints=gs.healthPoints-1

                pygame.display.flip()
                clk.tick(30)
                
            gs.getNextWord()

        if gs.healthPoints==0:
            screen.fill((0,0,0))
            Lose=Font.render("Sorry U Lose, click X to exit", True, (255, 0, 0))
            screen.blit(Lose,(width/2,height/2))

        if gs.currWord=='None':
            screen.fill((0,0,0))
            Won=Font.render("Congrats U won, click X to exit", True, (255, 0, 0))
            screen.blit(Won,(width/2,height/2))

        pygame.display.flip()
        clk.tick(30) 


# main function
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
            if 180 <= mouse[0] <= 180+65 and 200 <= mouse[1] <= 200+23:
                game("EASY")

        if event.type ==  pygame.MOUSEBUTTONDOWN:
            if 380 <= mouse[0] <= 380+101 and 200 <= mouse[1] <= 200+20:
                game("MEDIUM")

        if event.type ==  pygame.MOUSEBUTTONDOWN:
            if 600 <= mouse[0] <= 600+72 and 200 <= mouse[1] <= 200+20:
                game("HARD")                
            
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
        clk.tick(30)