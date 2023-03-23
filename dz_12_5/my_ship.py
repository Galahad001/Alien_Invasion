import pygame

class MyShip():
    def __init__(self, my_game):
        self.screen = my_game.screen
        self.seti = my_game.settings
        self.screen_rect = my_game.screen.get_rect()


        self.img = pygame.image.load('dz_12_5/ship2.bmp')
        self.re = self.img.get_rect()

        self.re.midleft = self.screen_rect.midleft



        self.moving_top = False 
        self.moving_bot =False


    def update(self):
        if self.moving_top and self.re.top > self.screen_rect.top:
            self.re. y -= self.seti.my_ship_speed
        if self.moving_bot and self.re.bottom < self.screen_rect.bottom:
            self.re. y += self.seti.my_ship_speed



    def blet(self):
        self.screen.blit(self.img, self.re)
        