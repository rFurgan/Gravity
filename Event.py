import pygame
import sys
from common import DIRECTION

class Event:
    def __init__(self, game):
        self.game = game

    def update_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # TODO
                    print("JUMP")
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.game.player.move(DIRECTION.LEFT)
        elif key[pygame.K_RIGHT]:
            self.game.player.move(DIRECTION.RIGHT)
        else:
            pass
