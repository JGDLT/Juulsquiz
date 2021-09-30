import pygame
pygame.init()#initializes Pygame
pygame.display.set_caption("Mouse events")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
draw = False

#color definitions (you have to add these to the game, and you can add more if you want)
BLUE = (0,0,200)
RED = (200, 0,0)
GREEN = (0,200, 0)
YELLOW = (200,122,50)
BLACK = (0,0,0)
WHITE = (200,200,200)
color = RED
#gameloop###################################################
while True:
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()
#update/timer section---------------------------------------    
    if mousePos[0] > 0 and mousePos[0] < 50 and mousePos[1] >750:
        color = RED
    if mousePos[0] > 50 and mousePos[0] < 100 and mousePos[1] >750:
        color = BLUE
    if mousePos[0] > 100 and mousePos[0] < 150 and mousePos[1] >750:
        color = GREEN
    if mousePos[0] > 150 and mousePos[0] < 200 and mousePos[1] >750:
        color = YELLOW
    if mousePos[0] > 200 and mousePos[0] < 250 and mousePos[1] >750:
        color = BLACK
    if mousePos[0] > 250 and mousePos[0] < 300 and mousePos[1] >750:
        color = WHITE
#input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        draw = True

    if event.type == pygame.MOUSEBUTTONUP:
        draw = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
 
#render section---------------------------------------------
    if draw == True:
        pygame.draw.circle(screen, color, (mousePos), 10) #player paintbrush
    
    #color changing rectangles at bottom of screen 
    pygame.draw.rect(screen, RED, (0,750,50,50))
    pygame.draw.rect(screen, BLUE, (50, 750, 50, 50))
    pygame.draw.rect(screen, GREEN, (100, 750, 50, 50))
    pygame.draw.rect(screen, YELLOW, (150,750, 50,50))
    pygame.draw.rect(screen, BLACK, (200,750, 50,50))
    pygame.draw.rect(screen, WHITE, (200,750, 5,50))
    pygame.draw.rect(screen, WHITE, (250,750, 5,50))
    pygame.draw.rect(screen, WHITE, (200,750, 50,5))
    pygame.draw.rect(screen, WHITE, (200,795, 50,5))
    pygame.display.flip()
    

#end game loop##############################################

pygame.quit()
