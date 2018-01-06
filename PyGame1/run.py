import pygame
import sys

from circles_main import Circles_main

class Game(object):
    def __init__(self,level):
        #config
        pygame.display.set_caption("NanoWar")
        self.tps_max = 60.0
        # init
        self.screen_weight = 1280
        self.screen_height = 720
        self.screen =  pygame.display.set_mode((self.screen_weight,self.screen_height))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0


        ##############  levels  ####################
        self.level = level
        self.lvl = Circles_main(self)





        ####text on screen######
        pygame.font.init()
        self.array_of_texts = []
        self.font = pygame.font.SysFont('Comic Sans MS', 30)


        background = pygame.image.load("graphic//background.jpg")
        Backgrond = pygame.Surface(background.get_size(),pygame.HWSURFACE)
        Backgrond.blit(background,(0,0))


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    self.t = 2


                    # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            self.screen.blit(Backgrond,(0,0))

            self.printing_messages()
            self.draw()


            self.write()
            a = True
            for i in range(len(self.lvl.circles) - 1):
                if(self.lvl.circles[i].side != "player"):
                    a = False
                    break
            if(a):
                self.level += 1
              #  sys.exit(0)

            pygame.display.flip()
    def write(self):
        for i in range (len(self.lvl.circles)):
            circle = self.lvl.circles[i]
            tekst = str(int(circle.range))
            if(circle.side == "player"):
                color = (255,255,255)
            elif(circle.side == "enemy"):
                color = (150,250,140)
            elif(circle.side == "enemy2"):
                color = (50,150,200)
            else:
                color = (0,0,0)
            self.textsurface = self.font.render(tekst, False, color)
            self.screen.blit(self.textsurface, (circle.pos_x - 13, circle.pos_y - 16))

    def message_to_screen(self,tekst,x,y):
        textsurface = self.font.render(tekst, False, (0, 0, 0))
        self.array_of_texts += self.screen.blit(textsurface,(x,y))

    def printing_messages(self):
        for i in range(len(self.array_of_texts)):
            self.array_of_texts[i]



    def tick(self):

        self.lvl.tick(self)



    def draw(self):
        self.lvl.draw()



if (__name__=="__main__"):
    print("wybierz poziom")
    print("1 - 6")
    a = int(input())
    Game(a)




