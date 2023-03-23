import pygame

class Go():
    def __init__(self, racet):
        self.screen = racet.screen
        self.screen_rect = racet.screen.get_rect()

        self.img = pygame.image.load('images/ship.bmp')
        self.rec = self.img.get_rect()

        self.rec.center = self.screen_rect.center

        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bot = False 


    def update(self):
        if self.moving_right and self.rec.right < self.screen_rect.right:
            self.rec.x += 4
        if self.moving_left and self.rec.left > 0:
            self.rec.x -= 4
        if self.moving_top and self.rec.top > self.screen_rect.top:
            self.rec.y -= 4
        if self.moving_bot and self.rec.bottom < self.screen_rect.bottom:
            self.rec.y += 4


    def blet(self):
        self.screen.blit(self.img, self.rec)