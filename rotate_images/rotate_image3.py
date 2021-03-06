# Auther      : Heinz Samuelsson
# Date        : 2015-08-02
# File        : rotate_image3.py
# Reference   : -
# Description : Rotate the loaded image at an offset position.
#               The position is set by offsetX and offsetY.
#               Same as rotation_image2 but now rotating without mouse control.
#               Instead the rotation speed is set by TIME_DELAY_IN_MS.
#
#               The offset can be changed by 1-5.
#               Type 'r' to rotate step by step.
#               Type 'c' to rotate continously.
#               Type 's' to stop rotation.
#               Type 'esc' to exit application.
#
#               Using rotozoom() instead of rotate() gives a better result.
#
#               If numpy is not installed then there is a possibility to use
#               a more conventional method. See comments below.
# Python ver : 2.7.3 (gcc 4.6.3)

import pygame
import sys
import math
import os
from pygame.locals import *  # remember to comment this and the next line if numpy is not used
import numpy as np

# define colors
RED         = (255, 0, 0)
GREEN       = (0, 255, 0)
BLUE        = (0, 0, 255)
LIGHT_BLUE  = (0, 255, 255)
BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)

TIME_DELAY_IN_MS = 100
WIDTH            = 640      # screen width
HEIGHT           = 360      # screen height
SCREEN_ORIGO     = (0,0)    # screen origo, upper left corner
LINE_WIDTH       = 2        # line width


# ---------------------------------------------------------------------------
# draw a crossing line in the middle of the screen
# ---------------------------------------------------------------------------
def draw_cross_line(screen):
    pygame.draw.line(screen, BLUE, (10,HEIGHT/2), (WIDTH-10,HEIGHT/2), 2)
    pygame.draw.line(screen, BLUE, (WIDTH/2,10), (WIDTH/2,WIDTH-10), 2)


# ---------------------------------------------------------------------------
# scan keyboard
# ---------------------------------------------------------------------------
def scan_keyboard():

    # static variables
    if not hasattr(scan_keyboard, "cKeyTyped"):
        scan_keyboard.cKeyTyped = False

    if not hasattr(scan_keyboard, "offsetX"):
        scan_keyboard.offsetX = 0

    if not hasattr(scan_keyboard, "offsetY"):
        scan_keyboard.offsetY = 0

    rKeyTyped = False
    rotateDir = 3     # rotation direction 1=LEFT, 2=RIGHT, 3=dummy
    newOffset = False # offset of needle (key 1-7)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        # rotate in increments
        elif event.type == KEYDOWN and event.key == pygame.K_r:
            rKeyTyped = True
            rotateDir = 1

        # rotate in increments
        elif event.type == KEYDOWN and event.key == pygame.K_t:
            rKeyTyped = True
            rotateDir = 2

        # rotate in continously
        elif event.type == KEYDOWN and event.key == pygame.K_c:
            scan_keyboard.cKeyTyped = True

        # stop continously rotation
        elif event.type == KEYDOWN and event.key == pygame.K_s:
            scan_keyboard.cKeyTyped = False

        # change offset to the middle of the image
        elif event.type == KEYDOWN and event.key == pygame.K_1:
            scan_keyboard.offsetX = 0
            scan_keyboard.offsetY = 0
            newOffset = True

        elif event.type == KEYDOWN and event.key == pygame.K_2:
            scan_keyboard.offsetX = 10
            scan_keyboard.offsetY = 10
            newOffset = True

        elif event.type == KEYDOWN and event.key == pygame.K_3:
            scan_keyboard.offsetX = 20
            scan_keyboard.offsetY = 20
            newOffset = True

        elif event.type == KEYDOWN and event.key == pygame.K_4:
            scan_keyboard.offsetX = 30
            scan_keyboard.offsetY = 30
            newOffset = True

        elif event.type == KEYDOWN and event.key == pygame.K_5:
            scan_keyboard.offsetX = 40
            scan_keyboard.offsetY = 40
            newOffset = True

        elif event.type == KEYDOWN and event.key == pygame.K_6:
            scan_keyboard.offsetX = 50
            scan_keyboard.offsetY = 50
            newOffset = True

        elif event.type == KEYDOWN and event.key == pygame.K_7:
            scan_keyboard.offsetX = 90
            scan_keyboard.offsetY = 90
            newOffset = True

        elif event.type == KEYDOWN and event.key == pygame.K_6:
            scan_keyboard.offsetX = 120
            scan_keyboard.offsetY = 120
            newOffset = True

        elif event.type == KEYDOWN and event.key == pygame.K_7:
            scan_keyboard.offsetX = 160
            scan_keyboard.offsetY = 160
            newOffset = True

    return newOffset, scan_keyboard.offsetX, scan_keyboard.offsetY, rotateDir, rKeyTyped, scan_keyboard.cKeyTyped


# ---------------------------------------------------------------------------
# main()
# input parameter 'arg' can be used for test purpose
# ---------------------------------------------------------------------------
def main(arg):

    # set rotation offset
    # if offset = 0 the rotation is around the center of the image
    # the green/red rectangles will be equal
    offsetX = 0
    offsetY = 0
    
    # position window on monitor
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" %(800,100)
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    screen_rect = screen.get_rect()
    
    pygame.display.set_caption(50*' '+'--- Rotate image ---')
    
    # choose among these images for rotation
    #image = pygame.image.load('green_car.png')
    image = pygame.image.load('white_needle1.png')
    #image = pygame.image.load('red_box_100x100.png')
    
    # if convert() is added then the green rectangle is partly hidden by the red rectangle
    # when using the convert function the alignment of the needle got a lot worse!
    #image = pygame.image.load('white_needle1.png').convert()
    
    imageRectangle = image.get_rect()
    center = imageRectangle.center
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    
    angle     = 0
    rKeyTyped = False  # if 'r' is typed => rotate one step
    newAngle  = 0
    oldAngle  = 99
    dirTemp   = 1      # temp variable to hold direction

    while True:
    
        # scan keyboard
        newOffset, offsetX, offsetY, rotateDir, rKeyTyped, cKeyTyped = scan_keyboard()
    
        # check if key is typed and act upon that 
        if rKeyTyped == True:
            if rotateDir == 1:
                angle += 5
                dirTemp = rotateDir
            elif rotateDir == 2:
                angle -= 5
                dirTemp = rotateDir
            else:
                pass
    
        elif cKeyTyped:
            if dirTemp == 1:
                angle += 5
            elif dirTemp == 2:
                angle -= 5
            else:
               pass
      
        # make sure angle is between 0-360
        angle = angle%360
        # remove flag and update new angle
        rKeyTyped = False
        newAngle  = angle
    
        screen.fill(BLACK)
    
        #rotatedImage = pygame.transform.rotate(image, angle)
        rotatedImage = pygame.transform.rotozoom(image, angle, 1)
        rotatedImageRectangle = rotatedImage.get_rect()
    
        # these calculations are used when numpy is *not* used
        radAngle = math.radians(angle)
        xPos = math.cos(radAngle)*offsetX
        yPos = math.sin(radAngle)*offsetY
    
        rotatedImageRectangle.center = (WIDTH/2, HEIGHT/2)
    
        # draw a rectangle before compensation of the angle
        pygame.draw.rect(screen, GREEN, (rotatedImageRectangle[0],
                                         rotatedImageRectangle[1],
                                         rotatedImageRectangle[2],
                                         rotatedImageRectangle[3]), 1)
    
        if newAngle != oldAngle or newOffset:
            print '-'*60
            print 'angle:',angle,'  -  xPos:',xPos,'  -  yPos:',yPos
            print '  Green rectangle before update:',rotatedImageRectangle
            print '  New x:',rotatedImageRectangle[0]+xPos
            print '  New y:',rotatedImageRectangle[1]-yPos
            print '  Rect width:',rotatedImageRectangle.width
            print '  Rect height:',rotatedImageRectangle.height
    
        # draw a line from SCREEN_ORIGO to the upper left rectangle
        pygame.draw.line(screen, LIGHT_BLUE, SCREEN_ORIGO, (rotatedImageRectangle[0],rotatedImageRectangle[1]), LINE_WIDTH)
        
        # ------------------------------------------------------------------------------------------------------
        # Now compensate rectangle due to the angle.
        # Only indexes [0] and [1] in rotatedImageRectangle are updated.
        # ------------------------------------------------------------------------------------------------------
    
        # if numpy, 1st method, is out of option then use the 2nd method
        # *** 1st method ***
        rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * offsetX,
                                       -np.sin(math.radians(angle)) * offsetY])
    
        # *** 2nd method ***
        # either use centerx/centery or center
        #rotatedImageRectangle.centerx = (rotatedImageRectangle[0]+xPos)
        #rotatedImageRectangle.centery = (rotatedImageRectangle[1]+yPos)
        #rotatedImageRectangle.center = (WIDTH/2+xPos, HEIGHT/2-yPos)
        
        if newAngle != oldAngle or newOffset:
            print '  Red rectangle after update:',rotatedImageRectangle
            newOffset = False
    
        oldAngle = newAngle
    
        # blit rotated image
        screen.blit(rotatedImage, rotatedImageRectangle)
    
        # draw a rectangle around the image after compensation of the angle
        pygame.draw.rect(screen, RED, (rotatedImageRectangle[0],
                                       rotatedImageRectangle[1],
                                       rotatedImageRectangle[2],
                                       rotatedImageRectangle[3]),
                                       1)
    
        # draw a line from SCREEN_ORIGO to the upper left rectangle
        pygame.draw.line(screen, LIGHT_BLUE, (0,0), (rotatedImageRectangle[0],rotatedImageRectangle[1]), 2)
        draw_cross_line(screen)
    
        pygame.display.update()
        pygame.time.delay(TIME_DELAY_IN_MS)


if __name__ == '__main__':
    main(sys.argv[1:])
