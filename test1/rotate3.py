import math
import pygame
import sys
from pygame.locals import *

# define colors
RED  = (255,0,0)
BLUE = (0,0,255)

pygame.init()
screen = pygame.display.set_mode((800,800),0,32)


def rotate_vector(angle,dx,dy):
    xNorm  = dx * math.cos(math.radians(angle)) - dy * math.sin(math.radians(angle))
    yNorm  = dx * math.sin(math.radians(angle)) + dy * math.cos(math.radians(angle))
    radius = math.sqrt(dx*dx + dy*dy)
    return xNorm, yNorm, radius


def move_vector(xOrig, yOrig, a, b):
    x = xOrig + a
    y = yOrig - b
    return x,y
    
# set origo
xOrigo = 100 
yOrigo = 500

# rotate angel
angle = 0

# size of vector
dx = 444 
dy = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print pos

    # calculate new coordinates
    xNorm, yNorm, radius = rotate_vector(angle,dx,dy)

    # move to new origo position
    x, y = move_vector(xOrigo, yOrigo, xNorm, yNorm)

    pygame.draw.rect(screen, BLUE, ((xOrigo,yOrigo-dx), (dx,dx)), 2)
    pygame.draw.line(screen, RED,  (xOrigo,yOrigo), (x,y), 2)

    angle += 10
    if angle == 100:
        angle = 0

    pygame.display.update()

