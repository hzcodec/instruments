import pygame
import pygame.locals
 
WHITE = (255, 255, 255)
 
pygame.init()
 
display  = pygame.display.set_mode((600, 600))
fpsClock = pygame.time.Clock()
 
image = pygame.image.load('blue_arrow.png')
print 'Image size:',image.get_rect()

xPos             = 300    # x position for arrow
yPos             = 300    # y position for arrow
angle            = 260     # start angle
idx              = 0      # index
spinn            = 0      # spinning counter
reducedSpeed     = 0      # new reduced speed => new angle
noOfSpinningLaps = 145    # number of laps before arrow starts to slow down
rotateSpeed      = 6      # initial rotation speed (angle)
scaleFactor      = 0.02   # reduce factor, how fast arrow is slowed down
stoppSpeed       = 0.02   # final stopp

while 1:
 
    display.fill(WHITE)
    rotated_image = pygame.transform.rotozoom(image, angle, 0.5)

    rect = rotated_image.get_rect()
    rect.center = (300,300)

    display.blit(rotated_image, rect)

    pygame.draw.line(display, (255,0,0), (300,10), (300,590), 2)
    pygame.draw.line(display, (255,0,0), (10,300), (590,300), 2)
 
    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
 
    # rotate at max speed until noOfSpinningLaps is reached
    if spinn < noOfSpinningLaps:
        angle += rotateSpeed
        spinn += 1
        print 'Spinning'
 
    # then reduce speed until arrow is stopped
    else:
        reducedSpeed = rotateSpeed - scaleFactor * idx
        idx += 1
        print 'Slowing down'

        if reducedSpeed < stoppSpeed:
            reducedSpeed = 0

        angle += reducedSpeed

    pygame.display.update()
    fpsClock.tick(30)

