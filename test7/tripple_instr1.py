import numpy as np
import pygame
import pygame.locals
import sys
import math
import os

# import all defines and classes
from tripple_defines import *
from instrument import Instrument


def blit_idx():
    """
    Print out index number for each instrument
    """
    screen.blit(idx1, (165,165)) # add 250
    screen.blit(idx1, (415,165))
    screen.blit(idx1, (665,165))
    screen.blit(idx1, (915,165))

    screen.blit(idx2, (245,55))
    screen.blit(idx2, (495,55))
    screen.blit(idx2, (745,55))
    screen.blit(idx2, (995,55))

    screen.blit(idx3, (325,165))
    screen.blit(idx3, (575,165))
    screen.blit(idx3, (825,165))
    screen.blit(idx3, (1075,165))

    screen.blit(instrument1, (200,260))
    screen.blit(instrument2, (460,260))
    screen.blit(instrument3, (700,260))
    screen.blit(instrument4, (960,260))


# position window 
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d" % WINDOW_POS

pygame.init()
screen  = pygame.display.set_mode((WIDTH, HEIGHT))

fpsClock = pygame.time.Clock()

indexFont = pygame.font.SysFont("None",28)
idx1 = indexFont.render("1", 0, BLACK)
idx2 = indexFont.render("2", 0, BLACK)
idx3 = indexFont.render("3", 0, BLACK)
instrument1 = indexFont.render("Position 1", 0, WHITE)
instrument2 = indexFont.render("Position 2", 0, WHITE)
instrument3 = indexFont.render("Position 3", 0, WHITE)
instrument4 = indexFont.render("Position 4", 0, WHITE)

# load instrument image and get rectangle size
background = pygame.image.load("../pic/tripple.png")
bgRect     = background.get_rect()
 
# load needle for all instances of instrument
firstInstrument = Instrument(screen, '../pic/small_red_needle.png', FIRST_INSTRUMENT_MID_POINT, 1, 2)

secondInstrument = Instrument(screen, '../pic/small_red_needle.png', SECOND_INSTRUMENT_MID_POINT, 2, 2)
thirdInstrument = Instrument(screen, '../pic/small_red_needle.png', THIRD_INSTRUMENT_MID_POINT, 3, 1)
fourthInstrument = Instrument(screen, '../pic/small_red_needle.png', FOURTH_INSTRUMENT_MID_POINT, 4, 1)

# rotation point of instrument image
offset1 = 19
offset2 = 19
firstInstrumentdegAngle  = 0.0
secondInstrumentdegAngle = 0.0
thirdInstrumentdegAngle  = 0.0
fourthInstrumentdegAngle = 0.0

# set instrument at start position
degAngle = -20.0
firstInstrument.set_needle_position(degAngle)
secondInstrument.set_needle_position(degAngle)
thirdInstrument.set_needle_position(degAngle)
fourthInstrument.set_needle_position(degAngle)

# input data that will set the final position of needle
inputData = 0.0

while 1:
 
    # update each instrument
    screen.blit(background, bgRect)
    firstInstrument.instrument_update(firstInstrumentdegAngle)
    secondInstrument.instrument_update(secondInstrumentdegAngle)
    thirdInstrument.instrument_update(thirdInstrumentdegAngle)
    fourthInstrument.instrument_update(fourthInstrumentdegAngle)
    blit_idx()

    # check for events, [quit, mouse click]
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

        # reset the instruments
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            print 'Restart'
            firstInstrument.reset_parameters()
            secondInstrument.reset_parameters()
            thirdInstrument.reset_parameters()
            fourthInstrument.reset_parameters()

        # trig the instruments
        elif event.type == pygame.KEYDOWN:
   
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            if event.key == pygame.K_1:
                firstInstrument.set_flag(True)
                inputData = 1.1
                firstInstrumentdegAngle = -20*inputData + 220

            elif event.key == pygame.K_2:
                secondInstrument.set_flag(True)
                inputData = 6.4
                secondInstrumentdegAngle = -20*inputData + 220

            elif event.key == pygame.K_3:
                thirdInstrument.set_flag(True)
                inputData = 8.1
                thirdInstrumentdegAngle = -20*inputData + 220

            elif event.key == pygame.K_4:
                fourthInstrument.set_flag(True)
                inputData = 3.8
                fourthInstrumentdegAngle = -20*inputData + 220

    pygame.display.update()
    fpsClock.tick(30)

