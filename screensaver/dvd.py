#Plugins
from os import remove
from time import sleep
import pygame
import random

from pygame.constants import K_ESCAPE, K_SPACE, K_a

#Starts program
pygame.init()

#Loads dvd image
dvdImage = pygame.image.load('dvd.png')

#Game interface options
gameDisplay = pygame.display.set_mode((1280,720))
pygame.display.set_caption('DVD Screensaver')
pygame.display.set_icon(dvdImage)

#Sets colors in variables (R,G,B,A)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

R = 255
G = 255
B = 255

#Honestly I dont know what this does
clock = pygame.time.Clock()
crashed = False

#what
def dvd(x,y):
    gameDisplay.blit(dvdImage, (x,y))

#Removes semi-transparent pixels
i = 1
for i in range(1,255):
    var = pygame.PixelArray(dvdImage)
    var.replace((0,0,0,i), (0,0,0,0))
    i += 1

#Changes dvd color to white
var = pygame.PixelArray(dvdImage)
var.replace((black), (white))
del var

#I think this is the game
while not crashed:
    
    for event in pygame.event.get():
        #I think this stops the program if you close the window
        if event.type == pygame.QUIT:
            crashed = True

    #Start position of image
    x = (-5) #981 side
    y = (-5) #586 bottom

    #Displays game
    gameDisplay.fill(black) #background
    dvd(x,y) #dvd image

    #When a key is pressed
    pressed_keys = pygame.key.get_pressed()
    
    #When space is pressed
    if pressed_keys[K_SPACE]:
        #Logo color
        previousColor  = R, G, B #assigns previous color to variable
        R = random.randrange(0, 256) #random red
        G = random.randrange(0, 256) #random green
        B = random.randrange(0, 256) #random blue
        var = pygame.PixelArray(dvdImage) #I think this converts the image into pixels
        var.replace((previousColor), (R, G, B)) #replaces colors in image by the random ones
        del var #I think this converts the image back into an image

    #When escape is pressed
    if pressed_keys[K_ESCAPE]:
        quit()

    #Position
    x = 0
    y = 0
    speed = .4
    
    #Temp values to know which direction the logo is moving
    tempX = 0
    tempY = 0

    run = True

    while run:

        #print(tempX, tempY)
        #print(x, y)
        
        #Down right
        if tempX == 0 and tempY == 0:
            #Changes position
            x = x+speed
            y = y+speed

            #Updates display
            gameDisplay.fill(black)
            dvd(x, y)

            #Checks if border is hit
            if x >= 981:
                tempX = 1
            if y >= 586:
                tempY = 1


        #Up right
        elif tempX == 0 and tempY == 1:
            #Changes position
            x = x+speed
            y = y-speed

            #Updates display
            gameDisplay.fill(black)
            dvd(x, y)

            #Checks if border is hit
            if x >= 981:
                tempX = 1
            if y <= 0:
                tempY = 0


        #Up left 
        elif tempX == 1 and tempY == 1:
            #Changes position
            x = x-speed
            y = y-speed

            #Updates display
            gameDisplay.fill(black)
            dvd(x, y)

            #Checks if border is hit
            if x <= 0:
                tempX = 0
            if y <= 0:
                tempY = 0


        #Down left
        elif tempX == 1 and tempY == 0:
            #Changes position
            x = x-speed
            y = y+speed

            #Updates display
            gameDisplay.fill(black)
            dvd(x, y)

            #Checks if border is hit
            if x <= 0:
                tempX = 0
            if y >= 586:
                tempY = 1

        #Moves image
        pygame.display.update() #updates display
        #sleep(0.016)
    
    #Framerate I think 
    clock.tick(60) #60 times a second

#Exits program
pygame.quit()
quit()