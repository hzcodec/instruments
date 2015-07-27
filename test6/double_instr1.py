import numpy as np
import pygame
import pygame.locals
import sys
import math
import os

# import all defines and classes
from defines import *
from instrument import Instrument


# position window 
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d" % WINDOW_POS

pygame.init()
screen  = pygame.display.set_mode((WIDTH, HEIGHT))
fpsClock = pygame.time.Clock()

# load instrument image
background = pygame.image.load("../pic/double_instr.png")
bgRect     = background.get_rect()
 
# left instance of Instrument
leftInstrument = Instrument('../pic/red_needle.png', 1)
leftInstrument.set_flag(True)

# right instance of Instrument
rightInstrument = Instrument('../pic/red_needle.png', 4)
rightInstrument.set_flag(True)

# set midpoints for each instrument
leftDisplayMidPoint  = LEFT_INSTRUMENT_MID_POINT
rightDisplayMidPoint = RIGHT_INSTRUMENT_MID_POINT

# rotation point of instrument image
offset1 = 99
offset2 = 99

# set leftInstrument at start position
degAngle = -20.0
leftInstrument.set_needle_position(degAngle)
rightInstrument.set_needle_position(degAngle)

# input data that will set the final position of needle
inputData = 0.0


while 1:
 
    screen.blit(background, bgRect)

    needleImage2, needleRect2 = rightInstrument.rotate(degAngle) 
    rightInstrument.rot(needleImage2, needleRect2, rightDisplayMidPoint, offset1, offset2)
    rightInstrument.blit_needle(screen, needleImage2, needleRect2)

    needleImage, needleRect = leftInstrument.rotate(degAngle) 
    leftInstrument.rot(needleImage, needleRect, leftDisplayMidPoint, offset1, offset2)
    leftInstrument.blit_needle(screen, needleImage, needleRect)

    # check for events, [quit, mouse click]
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

        # reset the leftInstrument
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            print 'Restart'
            leftInstrument.reset_parameters()
            rightInstrument.reset_parameters()

        elif event.type == pygame.KEYDOWN:
   
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            if event.key == pygame.K_1:
                leftInstrument.set_flag(True)
                rightInstrument.set_flag(True)
                inputData = 1.0 

            elif event.key == pygame.K_2:
                leftInstrument.set_flag(True)
                inputData = 2.8

            elif event.key == pygame.K_3:
                rightInstrument.set_flag(True)
                inputData = 6.0

            y = -20*inputData + 220
            degAngle = y

    pygame.display.update()
    fpsClock.tick(30)

