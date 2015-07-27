import os
import sys
import math
import pygame
import inspect

WHITE = (255,255,255)


class Rotator(object):
    def __init__(self, center, origin):
        x_mag = center[0] - origin[0]
        y_mag = center[1] - origin[1]

        self.radius = math.hypot(x_mag, y_mag)
        self.start_angle = math.atan2(-y_mag, x_mag)
        print inspect.stack()[0][3],'(): center =',center,' origin =',origin
        print inspect.stack()[0][3],'(): x_mag =',x_mag,' y_mag =',y_mag
        print inspect.stack()[0][3],'(): radius =',self.radius,' start_angle =',self.start_angle
        print inspect.stack()[0][3],'(): center =',center,' origin =',origin,' x_mag =',x_mag,' y_mag =',y_mag

    def __call__(self, angle, origin):

        new_angle = math.radians(angle) + self.start_angle
        #new_x = origin[0] + self.radius*math.cos(new_angle)
        #new_y = origin[1] - self.radius*math.sin(new_angle)
        new_x = 250 + self.radius*math.cos(new_angle)
        new_y = 250 - self.radius*math.sin(new_angle)
        #print inspect.stack()[0][3],'(): new_angle=',new_angle,' angle =',angle,' start_angle =',self.start_angle
        #print inspect.stack()[0][3],'(): new_angle=',new_angle,' angle =',angle,' start_angle =',self.start_angle
        #print inspect.stack()[0][3],'(): angle =',angle,' origin =',origin,' new_x =',new_x,' new_y =',new_y
        return (new_x,new_y)


class Character(object):
    def __init__(self,image,location,origin="center"):
        self.original_image = image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=location)
        self.angle = 0
        self.set_origin(getattr(self.rect, origin))
        self.speed = 8
        self.speed_ang = 8 #1
        print inspect.stack()[0][3],'(): <Character> rect =',self.rect

    def set_origin(self, point):
        self.origin = list(point) # make a list (x,y) => [x,y]
        self.rotator = Rotator(self.rect.center, point)

        print inspect.stack()[0][3],'(): self.origin =',self.origin,' self.angle:',self.angle

    def rotate(self):
        self.angle = (self.angle+1)%360                                    # a way to count from 0 - 360, no need for if v=360
        new_center = self.rotator(self.angle, self.origin)                 #__call__ in Rotator is called
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=new_center)

    def update(self, surface):
        self.rotate()
        surface.blit(self.image, self.rect)
        pygame.draw.line(surface, (255,0,0), (250,10), (250,490), 2)
        pygame.draw.line(surface, (255,0,0), (10,250), (490,250), 2)


class Control(object):
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.fps = 30.0
        print inspect.stack()[0][3],'(): ',' screen_rect =',self.screen_rect

        self.actor = Character(LENA, self.screen_rect.center, "midbottom")


    def main_loop(self):
        while True:
            self.screen.fill(WHITE)
            self.actor.update(self.screen)

            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    os.environ["SDL_VIDEO_CENTERED"] = '1'
    pygame.init()
    pygame.display.set_mode((500,500))
    LENA = pygame.image.load("../pic/needle1.png").convert_alpha()
    run_it = Control()
    run_it.main_loop()
    pygame.quit()
    sys.exit()
