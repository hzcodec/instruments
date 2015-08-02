import pygame
import sys
from pygame.locals import *

# Rotate => boundary rectangle change => center change

# define colors
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RIGHT = 3

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
            print 'Current mouse position:',mousePos

        elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
            angle += 10
            print 'Right mouse button clicked'

        elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()


    screen.fill(BLACK)

    rotatedImage = pygame.transform.rotate(image, angle)
    rotatedImageRectangle = rotatedImage.get_rect()

    #rotatedImageRectangle.center = (mousePos[0],mousePos[1])
    rotatedImageRectangle.center = (320,180)

    screen.blit(rotatedImage, rotatedImageRectangle)

    pygame.display.update()
    pygame.time.delay(2)

