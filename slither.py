import pygame
import time
import random
from pygame import mixer
pygame.mixer.init()
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

Width = 800
Height = 600

gamedisplay = pygame.display.set_mode((Width,Height))

pygame.display.set_caption('slither')


#################################################################################
"""Music"""

#pygame.mixer.music.load("Game-Menu.mp3")
#pygame.mixer.music.set_volume(0.5)
#pygame.mixer.music.play(-1)


        


#################################################################################




BG = pygame.image.load("images/bg 4.jpg").convert()



    
start_bg = pygame.image.load("images/bg.jpg").convert()

appleimg = pygame.image.load('images/apple1.png')

icon = pygame.image.load('images/icon.jpg')

pygame.display.set_icon(icon)
                         

body = pygame.image.load('images/body.png')

img = pygame.image.load('images/snakehead.png')

clock  = pygame.time.Clock()

blocksize = 25
applethickness = 25
FPS = 10

direction = "right"
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

def pause():
    paused = True
    
    message_to_screen("Paused",white,-100,size="large")
    message_to_screen("Press C to continue or Q to quit",white,50,size = "small")
    pygame.display.update()
    
    while paused:
        pygame.mixer.music.pause()
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    pygame.mixer.music.unpause()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #gamedisplay.fill(white)
       
                        

    

def score(score):
    text = smallfont.render('Score: ' +str(score), True,white)
    gamedisplay.blit(text, [0,0])

def randAppleGen():
    randApplex = round(random.randrange(0 , Width-applethickness))
    randAppley = round(random.randrange(0 , Height-applethickness))

    return randApplex,randAppley



def game_intro():
    intro = True
    start_bg = pygame.image.load("images/bg.jpg")
    gamedisplay.blit(start_bg, (0,0))
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        message_to_screen("Welcome to Slither",
                          green,
                          -100,
                          size = "large")
        message_to_screen("The objective of the game is to eat red apples",
                          black,
                          -30)
        message_to_screen("The more apples you eat the longer you get",
                          black,
                          10)
        message_to_screen("if you run into yourself or the edges you die",
                          black,
                          50)
        message_to_screen("Press C to Play or Q to quit and P to pause",
                          black,
                          100)
           

    
        pygame.display.update()
        clock.tick(5)
def Snake (blocksize,snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)   

    gamedisplay.blit(head , (snakelist[-1][0], snakelist[-1][1]))
    """this is the snake displayed in the screen"""
    for xny in snakelist[:-1]:
        gamedisplay.blit(body , (xny[0],xny[1]))


def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
         textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color,y_displace=0, size = 'small'):
    textSurf,textRect = text_objects(msg,color,size)
    #screen_text = font.render (msg , True, color)
    #gamedisplay.blit(screen_text , [Width/2 , Height/2])#adding text to screen
    textRect.center = round((Width/2)), round((Height/2)) +y_displace
    gamedisplay.blit(textSurf, textRect)
    
# for quitting the display box using 'x' symbol
def gameLoop():
    #pygame.mixer.music.load("music.mp3")
    #pygame.mixer.music.set_volume(0.2)
    #pygame.mixer.music.play(-1)

    global direction
    direction = 'right'
    gameExit = False
    gameOver = False
    
        

    lead_x = Width/2 #1st block
    lead_y = Height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    

    randApplex = round(random.randrange(0 , Width-applethickness))#/10.0)*10.0
    randAppley = round(random.randrange(0 , Height-applethickness))#/10.0)*10.0


    randApplex , randAppley = randAppleGen()
    while not gameExit:
        while gameOver == True:
            pygame.mixer.music.pause()
            message_to_screen("Game over",
                              red,
                               -50,
                              size = 'large')
            message_to_screen("Press C to play or Q to quit", white,50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                gameOver = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change= -blocksize
                    lead_y_change= 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = blocksize
                    lead_y_change= 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change= -blocksize
                    lead_x_change=0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = blocksize
                    lead_x_change=0

                elif event.key == pygame.K_p:
                    
                    pause()
                elif event.key == pygame.K_h:
                    appleAnim.play()
                    showAnim = True
                    
        if lead_x >= Width or lead_x<0 or lead_y>=Height or lead_y < 0:
            gameOver = True
    
        lead_x += lead_x_change
        lead_y += lead_y_change
        ## Adding background image                
        BG = pygame.image.load ("images/bg 4.jpg")
        gamedisplay.blit(BG , (0,0))
        ##pygame.draw.rect(gamedisplay, red , [randApplex, randAppley ,blocksize,blocksize])

        gamedisplay.blit(appleimg, (randApplex , randAppley))




        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        
        Snake(blocksize , snakeList)

        score(snakeLength-1)
        #400,300 where the rectangle to be placed,10,10 is width and height
        pygame.display.update()
##         if lead_x == randApplex and lead_y == randAppley:
##            randApplex = round(random.randrange(0 , Width-blocksize)/10.0)*10.0
##            randAppley = round(random.randrange(0 , Height-blocksize)/10.0)*10.0
##            snakeLength +=1 
                                 

##        if lead_x >= randApplex and lead_x <= randApplex +applethickness:
##            if lead_y >=randAppley and lead_y <=randAppley + applethickness:
##                
##                randApplex = round(random.randrange(0 , Width-blocksize))
##                randAppley = round(random.randrange(0 , Height-blocksize)) 
##                snakeLength +=1
        """Logic for crossover of the snake"""
        """Top left of snake"""
        """Top right of snake"""
       
        if lead_x  > randApplex and lead_x <randApplex +applethickness or lead_x + blocksize > randApplex and lead_x + blocksize < randApplex + applethickness:
            if lead_y  > randAppley and lead_y <randAppley +applethickness or lead_y + blocksize > randAppley and lead_y + blocksize < randAppley + applethickness:
                randApplex,randAppley = randAppleGen() 
                snakeLength +=1
                pygame.mixer.Sound.play(pygame.mixer.Sound("music/eat.wav"))
                pygame.mixer.music.set_volume(0.9)
                
                
                
                
                
        


        
        clock.tick(FPS)
    
    pygame.quit()
    quit()


game_intro()
gameLoop()

  
