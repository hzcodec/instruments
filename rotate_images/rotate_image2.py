import pygame
import sys
from pygame.locals import *
import numpy as np
import math

# Rotate => boundary rectangle change => center change

# define colors
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RIGHT = 3

# set rotation offset
# if offset = 0 the rotation is around the middle of the image
offsetX = 20
offsetY = 20

pygame.init()
screen = pygame.display.set_mode((640, 360), 0, 32)
screen_rect = screen.get_rect()

image = pygame.image.load('green_car.png')

imageRectangle = image.get_rect()
center = imageRectangle.center

print 'Rectangle:',imageRectangle
print 'Center:',center

background = pygame.Surface(screen.get_size())

background = background.convert()
background.fill(WHITE)

angle = 0
mousePos = (0,0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEMOTION:
            mousePos = pygame.mouse.get_pos()

        elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
            angle += 10

        elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()


    screen.fill(BLACK)

    pygame.draw.line(screen, BLUE, (10,180), (630,180), 2)
    pygame.draw.line(screen, BLUE, (320,10), (320,350), 2)

    rotatedImage = pygame.transform.rotate(image, angle)
    #rotatedImage = pygame.transform.rotozoom(image, angle, 0.5)
    rotatedImageRectangle = rotatedImage.get_rect()

    rotatedImageRectangle.center = (320,180)
    rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * offsetX,
                                   -np.sin(math.radians(angle)) * offsetY])
    print 'Rectangle:',rotatedImageRectangle

    screen.blit(rotatedImage, rotatedImageRectangle)

    # draw a rectangle around the image
    pygame.draw.rect(screen, RED, (rotatedImageRectangle[0],
                                   rotatedImageRectangle[1],
                                   rotatedImageRectangle[2],
                                   rotatedImageRectangle[3]), 1)

    pygame.display.update()
    pygame.time.delay(2)

