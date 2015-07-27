import pygame
import pygame.locals
import random
import sys
 
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DISPLAY_SIZE = (600,600)


class GenerateAngle():

    def __init__(self):
        self.randomAngle = random.randrange(1,350,1) 
        self.randomSpinningLaps = random.randrange(30,250,1) 
        print 'Random angle:',self.randomAngle
        print 'Random laps:',self.randomSpinningLaps

    def __str__(self):
        return str(self.randomAngle)

    def get_random_numbers(self):
        return self.randomAngle, self.randomSpinningLaps
  
    def get_random_laps(self):
        self.randomSpinningLaps = random.randrange(30,250,1) 
        print 'Random laps:',self.randomSpinningLaps
        return self.randomSpinningLaps



class SpinningWheel():

    def __init__(self):
        
        # get a random generated angle
        self.rr = GenerateAngle()

        # start angle and number of laps before arrow starts to slow down
        self.startAngle, self.noOfSpinningLaps = self.rr.get_random_numbers()

        self.xPos            = 300                                      # x position for arrow
        self.yPos            = 300                                      # y position for arrow
        self.angle           = 260                                      # angle for arrow
        self.idx             = 0                                        # index
        self.spinn           = 0                                        # spinning counter
        self.startSpinning   = False                                    # flag to start spinnning arrow
        self.reducedSpeed    = 0                                        # new reduced speed => new angle
        self.rotateSpeed     = 8                                        # initial rotation speed (angle)
        self.scaleFactor     = 0.02                                     # reduce factor, how fast arrow is slowed down
        self.stoppSpeed      = 0.02                                     # final stopp
        self.display         = pygame.display.set_mode((DISPLAY_SIZE))  # set display size
        self.arrowImage      = pygame.image.load('blue_arrow.png')      # load arrow image
        self.backgroundImage = pygame.image.load('background.png').convert() # load background image
        pygame.init()
        pygame.display.set_caption('                                    --- SPINNING WHEEL ---')
        self.fpsClock = pygame.time.Clock()

    def check_keyboard(self):
        # check for quit
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_RIGHT:
                    self.startSpinning = True
                    print 'Start spinning'
   
    def calc_new_arrow_postion(self):
        # rotate at max speed until the number of spinnings is reached
        if self.spinn < self.noOfSpinningLaps:

            self.angle += self.rotateSpeed
            if self.angle > 359:
                self.angle = 0

            self.spinn += 1
            #print 'Spinning'
 
        # then reduce speed until arrow is stopped
        else:
            self.reducedSpeed = self.rotateSpeed - self.scaleFactor * self.idx
            self.idx += 1
            #print 'Slowing down'

            # now initialize all internal variable so we can start a new spinn
            if self.reducedSpeed < self.stoppSpeed:
                print ' '
                print 'Current angle:',self.angle
                self.reducedSpeed  = 0
                self.spinn         = 0
                self.idx           = 0
                self.startAngle    = self.angle
                self.startSpinning = False

                # get a new number of spinning laps
                self.noOfSpinningLaps = self.rr.get_random_laps()

            self.angle += self.reducedSpeed
            if self.angle > 359:
                self.angle = 0

    def update(self):
        self.display.fill(WHITE)

        # start to spinn arrow
        if self.startSpinning:
            self.rotated_image = pygame.transform.rotozoom(self.arrowImage, self.angle, 0.5)
 
        # set arrow to start position
        else: 
            self.rotated_image = pygame.transform.rotozoom(self.arrowImage, self.startAngle, 0.5)
            self.angle = self.startAngle

        self.rect = self.rotated_image.get_rect()
        self.rect.center = (300,300)

        self.display.blit(self.backgroundImage, (0, 0))
        self.display.blit(self.rotated_image, self.rect)

        pygame.display.update()
        self.fpsClock.tick(30)

    def on_execute(self):
        while 1:
            self.check_keyboard()
            self.calc_new_arrow_postion()
            self.update()


def main():
    spinningWheel = SpinningWheel()
    spinningWheel.on_execute()
     

if __name__ == '__main__':
    main()

