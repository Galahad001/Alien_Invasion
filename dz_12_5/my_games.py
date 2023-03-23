import sys

import pygame

from my_settings import MySettings

from my_ship import MyShip

from my_bullet import MyBullet

class MyGame:
    def __init__(self):
        pygame.init()

        self.settings = MySettings()

        self.screen = pygame.display.set_mode((self.settings.screen_widht, self.settings.screen_height))
        pygame.display.set_caption("My Game Test")

        self.my_ship = MyShip(self)

        self.bullets = pygame.sprite.Group()



    def run_my_game(self):
        while True:
            self._check_events()
            self.my_ship.update()
            self._update_bullets()
            self._update_screen()
        

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type ==pygame.KEYUP:
                self._check_keyup_events(event)



    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.my_ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.my_ship.moving_bot = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

            

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.my_ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.my_ship.moving_bot = False

    def _fire_bullet(self):
        if len(self.bullets) <self.settings.bullets_allowed: 
            new_bullet = MyBullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_widht:
                self.bullets.remove(bullet)
            # print(len(self.bullets))


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        self.my_ship.blet()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        pygame.display.flip()

if __name__=="__main__":
    my_game = MyGame()
    my_game.run_my_game()
    