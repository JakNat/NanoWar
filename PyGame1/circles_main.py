from math import fabs, sqrt
from Circle import circle
from circle_interaction import action
import pygame
from pygame.math import Vector2

class Circles_main(object):

 ###############MAIN#######################
    def __init__(self,game):

        self.game = game
        x = self.game.screen_weight
        y = self.game.screen_height
        _x = int(x/10)
        _y = int(y/10)

        ############################ levels  ###########################################
        # level1
        if(self.game.level == 1):
            # tworzenie kół(bakterii)
            self.team1_1 = circle(game, _x, int(y / 2), 3, "player")
            self.team2_1 = circle(game, int(_x * 9), int(y / 2), 2, "enemy")
            self.neutral_1 = circle(game, int(_x * 3), int(_y * 2), 1, "neutral")
            self.neutral_2 = circle(game, int(_x * 3), int(_y * 8), 1, "neutral")
            self.neutral_3 = circle(game, int(_x * 6), int(_y * 2), 1, "neutral")
            self.neutral_4 = circle(game, int(_x * 6), int(_y * 8), 1, "neutral")
            # tablica wszystkich kół(bakterii)
            self.circles = [self.team1_1, self.neutral_1, self.neutral_2, self.team2_1, self.neutral_3, self.neutral_4]

            # Połączenie miedzy danymi kołami
            self.connectons_array = [self.team1_1, self.neutral_1,
                                     self.team1_1, self.neutral_2,
                                     self.neutral_1, self.neutral_3,
                                     self.neutral_2, self.neutral_4,
                                     self.neutral_1, self.neutral_2,
                                     self.neutral_3, self.team2_1,
                                     self.neutral_4, self.team2_1]

        #level 2
        if (self.game.level == 2):
            # tworzenie kół(bakterii)

            team1_1 = circle(game, _x, int(y / 2), 2, "player")
            team2_1 = circle(game, int(_x * 9), int(y / 2), 2, "enemy")
            neutral_1 = circle(game, int(_x * 3), int(_y * 2), 1, "neutral")
            neutral_2 = circle(game, int(_x * 3), int(_y * 8), 1, "neutral")
            neutral_3 = circle(game, int(_x * 6), int(_y * 2), 1, "neutral")
            neutral_4 = circle(game, int(_x * 6), int(_y * 8), 1, "neutral")
            team3_1 = circle(game, int(x / 2), int(y / 2), 3, "enemy2")
            # tablica wszystkich kół(bakterii)
            self.circles = [team1_1, neutral_1, neutral_2, team2_1, neutral_3, neutral_4, team3_1]

            # Połączenie miedzy danymi kołami
            self.connectons_array = [team1_1, neutral_1,
                                     team1_1, neutral_2,
                                     neutral_1, neutral_3,
                                     neutral_2, neutral_4,
                                     neutral_1, neutral_2,
                                     neutral_3, team2_1,
                                     neutral_4, team2_1,
                                     team3_1, neutral_1,
                                     team3_1, neutral_2,
                                     team3_1, neutral_3,
                                     team3_1, neutral_4, ]

        #level 3
        if (self.game.level == 3):
            # tworzenie kół(bakterii)

            team1_1 = circle(game, _x * 2, _y, 2, "player")
            team1_2 = circle(game,_x * 2,_y * 4,1,"player")
            team1_3 = circle(game, _x *2, _y * 7, 1, "player")
            team1_4 = circle(game,_x * 5, _y * 7, 1, "player")


            team2_1 = circle(game, _x * 8, _y,4,"enemy")
            # tablica wszystkich kół(bakterii)
            self.circles = [team1_1, team1_2 , team1_3, team2_1, team1_4]

            # Połączenie miedzy danymi kołami
            self.connectons_array = [team1_1, team1_2,
                                     team1_2, team1_3,
                                     team1_3,team1_4,
                                     team1_4, team2_1
                                    ]
        # level 4
        if(self.game.level == 4):
            team1_1 = circle(game,_x * 5, _y * 2, 3, "player")
            neutral_1 = circle(game, _x * 2, _y * 4, 2, "neutral")
            neutral_2 = circle(game, _x * 8, _y * 4, 2, "neutral")
            team2_1 = circle(game,_x * 2, _y * 8, 2, "enemy")
            team2_2 = circle(game, _x * 8, _y * 8, 2, "enemy")

            self.circles = [team1_1, neutral_1, neutral_2, team2_1, team2_2]

            self.connectons_array = [team1_1, neutral_1,
                                     team1_1, neutral_2,
                                     team2_1, neutral_1,
                                     team2_2, neutral_2]
        # level 5
        if(self.game.level == 5):
            team1_1 = circle(game, _x * 5, _y * 2, 3, "enemy")
            neutral_1 = circle(game, _x * 2, _y * 4, 2, "neutral")
            neutral_2 = circle(game, _x * 8, _y * 4, 2, "neutral")
            team2_1 = circle(game, _x * 2, _y * 8, 2, "player")
            team2_2 = circle(game, _x * 8, _y * 8, 2, "player")

            self.circles = [team1_1, neutral_1, neutral_2, team2_1, team2_2]

            self.connectons_array = [team1_1, neutral_1,
                                     team1_1, neutral_2,
                                     team2_1, neutral_1,
                                     team2_2, neutral_2]
        # level 6
        if(self.game.level == 6):
            team1_1 = circle(game, _x * 5, _y * 5, 3, "player")

            neutral_1 = circle(game, _x * 3, _y * 1, 1 , "neutral")
            neutral_2 = circle(game, _x * 3, _y * 3, 1, "neutral")
            neutral_3 = circle(game, _x * 3, _y * 5, 1, "neutral")
            neutral_4 = circle(game, _x * 3, _y * 7, 1, "neutral")
            neutral_5 = circle(game, _x * 3, _y * 9, 1, "neutral")

            team2_1 = circle(game, _x, _y * 5 , 4, "enemy")

            neutral_6 = circle(game, _x * 7, _y * 1, 1, "neutral")
            neutral_7 = circle(game, _x * 7, _y * 3, 1, "neutral")
            neutral_8 = circle(game, _x * 7, _y * 5, 1, "neutral")
            neutral_9 = circle(game, _x * 7, _y * 7, 1, "neutral")
            neutral_10 = circle(game, _x * 7, _y * 9, 1, "neutral")

            team3_1 = circle(game, _x * 9, _y * 5, 4, "enemy2")

            self.circles = [team1_1, neutral_1, neutral_2, neutral_3 ,neutral_4, neutral_5
                            , neutral_6, neutral_7, neutral_8, neutral_9, neutral_10, team2_1, team3_1]
            self.connectons_array =[team1_1, neutral_1,team2_1,neutral_1,
                                    team1_1, neutral_2,team2_1,neutral_2,
                                     team1_1, neutral_3,team2_1,neutral_3,
                                      team1_1, neutral_4,team2_1,neutral_4,
                                      team1_1, neutral_5,team2_1,neutral_5,
                                      team1_1, neutral_6,team3_1,neutral_6,
                                      team1_1, neutral_7,team3_1,neutral_7,
                                      team1_1, neutral_8,team3_1,neutral_8,
                                      team1_1, neutral_9,team3_1,neutral_9,
                                      team1_1, neutral_10,team3_1,neutral_10 ]



        ##############################################################################


        #Global
        self.time = 1
        self.I = None
        self.actions = 0
        #### globalna do AI komputera######
        self.dzielnik = 2
    def tick(self,game):
        #input
        self.circles_interactions()
        self.tickets_circles()

        if(self.time % 200 == 0):
            self.enemy_move()
        self.time += 1


    def draw(self):
        self.drawingLines()
        self.drawing_circles()


    ##################### methods #########################

    """def action(self,circle1):

        click = pygame.mouse.get_pressed()
        if(circle1.promien() < circle1.range):
            if(click[0] == 1):
                circle1.color = (0,0,0)
        elif (circle1.promien() > circle1.range and circle1.color == (0,0,0)):
            if (click[0] == 1):
                circle1.color = circle1.main_color"""

    def drawingLines(self):
        for i in range(len(self.connectons_array) - 1):
            if (i % 2 == 0):
                circle1 = self.connectons_array[i]
                circle2 = self.connectons_array[i + 1]
                if(circle1.side == "player" and circle2.side == "player"):
                    pygame.draw.line(self.game.screen, (0, 0, 255),
                                     (circle1.pos_x, circle1.pos_y)
                                     , (circle2.pos_x, circle2.pos_y), 5)
                elif (circle1.side == "enemy" and circle2.side == "enemy"):
                    pygame.draw.line(self.game.screen, (255, 0, 0),
                                     (circle1.pos_x, circle1.pos_y)
                                     , (circle2.pos_x, circle2.pos_y), 5)
                elif (circle1.side == "enemy" and circle2.side == "enemy"):
                    pygame.draw.line(self.game.screen, (255, 0, 0),
                                     (circle1.pos_x, circle1.pos_y)
                                     , (circle2.pos_x, circle2.pos_y), 5)
                elif (circle1.side == "enemy2" and circle2.side == "enemy2"):
                    pygame.draw.line(self.game.screen, (55, 0, 0),
                                     (circle1.pos_x, circle1.pos_y)
                                     , (circle2.pos_x, circle2.pos_y), 5)

                else:
                    pygame.draw.line(self.game.screen, (0, 0, 0),
                                     (circle1.pos_x, circle1.pos_y)
                                     , (circle2.pos_x, circle2.pos_y), 5)

    def circles_interactions(self):
        for i in range(len(self.connectons_array)):
            if (i % 2 == 0):
                if (self.connectons_array[i].side == "player"):
                    self.action = action(self,self.connectons_array[i],self.connectons_array[i + 1])
                    self.connectons_array[i].move(self.connectons_array[i+1])

                if (self.connectons_array[i + 1].side == "player"):
                    self.connectons_array[i + 1].move(self.connectons_array[i])

    def enemy_move(self):
        ############# AI komputera ###########
        for j in range(2):

            if(j == 0):
                side = "enemy"
            if(j == 1):
                side = "enemy2"

            for i in range(len(self.connectons_array)):
                if (i % self.dzielnik == 0):
                    circle1 = self.connectons_array[i]
                    circle2 = self.connectons_array[i + 1]
                    if (circle1.side == side and (circle1.range > 15 or (circle1.range / 2) > circle2.range ) and circle2.side != side):
                        circle1.move_enemy(circle2, side)

                    elif (circle1.side != side and (circle2.range > 15 or (circle2.range / 2) > circle1.range ) and circle2.side == side):
                        circle2.move_enemy(circle1, side)
                    elif(circle1.side == side and circle2.side and(circle1.range > 15 or circle2.range > 15)):
                        if ( circle1.range > circle2.range):
                            circle1.move_enemy(circle2, side)
                        else:
                            circle2.move_enemy(circle1,side)
                if(self.dzielnik == 2):
                     a = 4
                if(self.dzielnik == 4):
                     a = 2
                self.dzielnik = a


    """def drawing_animation(self):
        for i in range(len(self.animation_array) - 1):
            self.animation_array[i].draw()"""

    def drawing_circles(self):
        for i in range(len(self.circles) ):
            self.circles[i].draw()
    def tickets_circles(self):
        for i in range(len(self.circles) ):
            self.circles[i].tick()


       # self.bakteria = self.load_texture("graphic//bakteria2.png", int(self.rangeI))
        #game.screen.blit(self.bakteria, (int(game.screen_weight / 2) - self.state_positionI, int(game.screen_height / 2) - self.state_positionI))