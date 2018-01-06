from math import fabs

import pygame

class action:
    def __init__(self, game, circle_from, circle_to):
        self.game = game
        self.circle1 = circle_from
        self.circle2 = circle_to
        self.x_max = fabs(self.circle1.pos_x - self.circle2.pos_x)
        self.y_max = fabs(self.circle1.pos_y - self.circle2.pos_y)
        self.x = 0
        self.y = 0
        self.const = self.x_max + self.y_max
        self._const = 0

    def tick(self):
        if (self.x < self.x_max):
            self.x += 1
        if (self.y < self.y_max):
            self.y += 1
        if (self._const < self.const):
            self._const +=1
        #print(self._const)
        self.wspolczynnik = self._const / self.const


        #print(self.wspolczynnik)
    def draw(self):
        if (self.x != self.x_max or self.y != self.y_max):
            pygame.draw.circle(self.game.screen, self.circle1.color, (int(200 + int(self.wspolczynnik * self.x_max)), int(200 + int(self.wspolczynnik * self.y))), int(self.circle1.range /2 ), 0)
        elif(self.x == self.x_max or self.y == self.y_max):

            self.x += 1
            self.y += 1
