from math import fabs, sqrt
import time

import pygame
from pygame.math import Vector2
class circle(object):

    def __init__(self,game, pos_x, pos_y,type,side):
        # type - rodzaj koła - od tego zalezy rozmiar oraz szybkoc rozrastania

        self.game = game
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.type = type
        self.range = self.range_type()
        self.color = self.color_type(side)
        self.side = side
        self.main_color = self.color = self.color_type(side)
        self.real_range = self.range_type()

    def tick(self):
        # input

        if (self.side != "neutral"):
            self.growing()
        self.action()
        # fizyka
        if (self.range < 0.0):
            self.range = 0.0
        if (self.range > 300.0):
            self.range = 350.0
        self.red = int(255 * (1 - (self.range / 100)))

    def draw(self):
        pygame.draw.circle(self.game.screen, self.color, (self.pos_x, self.pos_y), int(self.real_range) + 35, 0)


############### methods ####################
    def action(self):

        click = pygame.mouse.get_pressed()
        if(self.promien() < self.real_range + 35):
            if(click[0] == 1):
                self.color = (0, 0, 0)

        elif (self.promien() > self.real_range + 35 and self.color == (0, 0, 0)):
            if (click[0] == 1):
                self.color = self.main_color

    def move(self,circle):

        click = pygame.mouse.get_pressed()

        if (circle.promien() < (self.real_range + 35)):
            if (click[0] == 1):


                if (self.color == (0, 0, 0)):
                    moving_cirle_range = self.range/2
                    if(circle.side != "player"):
                        if (circle.range < moving_cirle_range):
                            circle.range = fabs(circle.range - moving_cirle_range)
                            circle.side = "player"
                            circle.main_color = self.main_color
                            circle.color = self.color

                        else:
                            circle.range -= moving_cirle_range
                    else:
                        circle.range += moving_cirle_range
                    self.range -= moving_cirle_range

    def move_enemy(self,circle,side):
        moving_cirle_range = self.range/2
        if (circle.side != side):
            if (circle.range < moving_cirle_range):
                circle.range = fabs(circle.range - moving_cirle_range)
                circle.side = side
                circle.color = self.color
                circle.main_color = self.main_color
            else:
                circle.range -= moving_cirle_range
        else:
            circle.range += moving_cirle_range
        self.range -= moving_cirle_range

    def promien(self):
        mouse = pygame.mouse.get_pos()
        self.mouse_x = mouse[0]
        self.mouse_y = mouse[1]
        a = fabs(self.mouse_x - self.pos_x)
        b = fabs(self.mouse_y - self.pos_y)
        c = sqrt((a * a) + (b * b))
        return c

    def range_type(self):

        if(self.type == 1):
            a = 25

        elif (self.type == 2):
            a = 40
        elif (self.type== 3):
            a = 60
        elif(self.type== 4):
            a = 80
        else:
            a = self.type
        return a



    def color_type(self,side):
        if (side == "player"):
            return (0,0,255)
        if (side == "neutral"):
            return (0,255,0)
        if (side == "enemy"):
            return (255,0,0)
        if (side == "enemy2"):
            return (155,155,0)





    def growing(self):
        if(self.type == 1):
            self.range += 1/120
        elif (self.type == 2):
            self.range += 1 / 90
        elif (self.type == 3):
            self.range += 1 / 75
        elif (self.type == 4):
            self.range += 1 / 40
        else:
            self.range += 1/100

