import sys

import pygame

class Scr:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((900, 400))
        pygame.display.set_caption("Test")


    def run(self):
        while True:
            self._check_events()
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
        if event.key == pygame.K_RIGHT:
            print("Down-right", event.key)
        elif event.key == pygame.K_LEFT:
            print("Down-left", event.key)
        elif event.key == pygame.K_UP: 
            print("Down-top", event.key)
        elif event.key == pygame.K_DOWN:
            print("Down-bottom", event.key)
        elif event.key == pygame.K_q:
            sys.exit()
        
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            print("UP-right", event.key)
        elif event.key == pygame.K_LEFT:
            print("UP-left", event.key)
        elif event.key == pygame.K_UP:
            print("UP-top", event.key)
        elif event.key == pygame.K_DOWN:
            print("UP-bottom", event.key)
                
    def _update_screen(self):
        pygame.display.flip()


if __name__=="__main__":
    dz = Scr()
    dz.run()