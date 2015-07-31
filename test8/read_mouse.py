import numpy as np
import pygame
import pygame.locals
import sys
import math
import os

# import all defines and classes
from defines import *
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
#    screen.blit(instrument3, (700,260))
#    screen.blit(instrument4, (960,260))


# position window 
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d" % WINDOW_POS

pygame.init()

# set screen
screen  = pygame.display.set_mode((1400, 600))

fpsClock = pygame.time.Clock()

# define font
indexFont = pygame.font.SysFont("None",28)
idx1 = indexFont.render("1", 0, BLACK)
idx2 = indexFont.render("2", 0, BLACK)
idx3 = indexFont.render("3", 0, BLACK)
instrument1 = indexFont.render("Mouse X-pos", 0, RED)
instrument2 = indexFont.render("Mouse Y-pos", 0, GREEN)

# load instrument image and get rectangle size
background = pygame.image.load("../pic/tripple.png")
bgRect     = background.get_rect()
 
# generate instances for all instruments
# input parameters: surface name, image, mid point, instrument index, speed
firstInstrument  = Instrument(screen, '../pic/small_red_needle.png', FIRST_INSTRUMENT_MID_POINT,  1, TEST_ROT_SPEED)
#secondInstrument = Instrument(screen, '../pic/small_red_needle.png', SECOND_INSTRUMENT_MID_POINT, 2, 2)

# initalize variables
firstInstrumentdegAngle  = 0
secondInstrumentdegAngle = 0.0

# set instrument at start position
degAngle = -20.0
firstInstrument.set_needle_position(degAngle)
#secondInstrument.set_needle_position(degAngle)

# input data that will set the final position of needle
inputData  = 0.0
mouseDataX = 0.0
mouseDataY = 0.0

while 1:
    # update each instrument
    screen.blit(background, bgRect)
    firstInstrument.instrument_update(firstInstrumentdegAngle)
    #secondInstrument.instrument_update(secondInstrumentdegAngle)
    pygame.draw.circle(screen, RED, (250,150), 15, 0)
    pygame.draw.circle(screen, BLACK, (250,150), 5, 0)
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
            #secondInstrument.reset_parameters()

        # trig the instruments
        elif event.type == pygame.KEYDOWN:
   
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            elif event.key == pygame.K_3:
                inputData = 6.8

            elif event.key == pygame.K_4:
                inputData = 3.8

        # set instrument 1 and 2 via mouse position
        elif event.type == pygame.MOUSEMOTION:
            # the factor 107: k = (1400-1) / (12-1)
            # the factor 46:  k = (600-1) / (12-1)
            # The size of the window is 1400x600

            mouseDataX = float(event.pos[0]) / 107.0
            mouseDataY = float(event.pos[1]) / 46.0

            # check boundaries
            if mouseDataX < 1.0:
                mouseDataX = 1.0
            elif mouseDataX > 12.0:
                mouseDataX = 12.0

#            if mouseDataY < 1.0:
#                mouseDataY = 1.0
#            elif mouseDataY > 12.0:
#                mouseDataY = 12.0

            #print float("{0:.1f}".format(mouseDataX))
            #print float("{0:.1f}".format(mouseDataY))

            firstInstrument.set_flag(True)
            inputData = float("{0:.1f}".format(mouseDataX))
            firstInstrumentdegAngle = int(-20*inputData + 220)
            print '1st angle:',firstInstrumentdegAngle

#            secondInstrument.set_flag(True)
#            inputData = float("{0:.1f}".format(mouseDataY))
#            secondInstrumentdegAngle = -20*inputData + 220

    pygame.display.update()
    fpsClock.tick(30)

