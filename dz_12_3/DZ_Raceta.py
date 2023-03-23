import sys

import pygame

from DZ_set import Set

from DZ_per import Go

class Raketa:
    def __init__(self):
        pygame.init()
        self.DZ_set = Set()

        self.screen = pygame.display.set_mode((self.DZ_set.screen_w, self.DZ_set.screen_h))
        pygame.display.set_caption("Project X")

        self.go = Go(self)


    def run(self):
        while True:
            self._check_events()
            self.go.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            self.go.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.go.moving_left = True
        elif event.key == pygame.K_UP:
            self.go.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.go.moving_bot = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.go.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.go.moving_left = False
        elif event.key == pygame.K_UP:
            self.go.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.go.moving_bot = False

    def _update_screen(self):
        self.screen.fill(self.DZ_set.bg_color)
        self.go.blet()
        pygame.display.flip()



if __name__=='__main__': 
    dz_r = Raketa()
    dz_r.run()