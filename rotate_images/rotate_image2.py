import pygame
import sys
from pygame.locals import *
import numpy as np
import math

# Rotate => boundary rectangle change => center change

# define colors
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RIGHT = 3

# set rotation offset
# if offset = 0 the rotation is around the middle of the image
# the green/red rectangles will be equal
offsetX = 30
offsetY = 30

pygame.init()
screen = pygame.display.set_mode((640, 360), 0, 32)
screen_rect = screen.get_rect()

image = pygame.image.load('green_car.png')

# if convert() is added then the green rectangle is partly hidden by the red rectangle
#image = pygame.image.load('green_car.png').convert()

imageRectangle = image.get_rect()
center = imageRectangle.center

print 'Rectangle:',imageRectangle
print 'Center:',center

background = pygame.Surface(screen.get_size())

background = background.convert()

angle = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
            angle += 10
            if angle > 360:
                angle = 0
          
            print 'angle:',angle

        elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()


    screen.fill(BLACK)

    pygame.draw.line(screen, BLUE, (10,180), (630,180), 2)
    pygame.draw.line(screen, BLUE, (320,10), (320,350), 2)

    rotatedImage = pygame.transform.rotate(image, angle)
    rotatedImageRectangle = rotatedImage.get_rect()

    radAngle = math.radians(angle)
    xPos = math.cos(radAngle)
    yPos = math.sin(radAngle)
    print 'xPos:',xPos*offsetX,'  -  yPos:',yPos*offsetY

    rotatedImageRectangle.center = (320,180)

    # draw a rectangle before compensation of the angle
    pygame.draw.rect(screen, GREEN, (rotatedImageRectangle[0],
                                   rotatedImageRectangle[1],
                                   rotatedImageRectangle[2],
                                   rotatedImageRectangle[3]), 1)
    #print 'Green rectangle before update:',rotatedImageRectangle
    
    # move rectangle according to the angle
    rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * offsetX,
                                   -np.sin(math.radians(angle)) * offsetY])

    #print '  Red rectangle after update:',rotatedImageRectangle

    # blit rotated image
    screen.blit(rotatedImage, rotatedImageRectangle)

    # draw a rectangle around the image after compensation of the angle
    pygame.draw.rect(screen, RED, (rotatedImageRectangle[0],
                                   rotatedImageRectangle[1],
                                   rotatedImageRectangle[2],
                                   rotatedImageRectangle[3]), 1)

    pygame.display.update()
    pygame.time.delay(2)

