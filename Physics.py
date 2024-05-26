import time
import pygame
from common import DIRECTION

class Physics:
    def __init__(self, game):
        self.game = game
        self.previous_seconds = time.monotonic()
        self.current_seconds = time.monotonic()
        self.delta_time = 0

    def update_gravity(self):
        for gravity_sprite in self.game.sprite.gravity_sprites:
            # TODO Needs further refinement
            if len(pygame.sprite.spritecollide(gravity_sprite, self.game.sprite.all_sprites, False)) <= 1:
                gravity_sprite.move(DIRECTION.DOWN)

    def update_delta_time(self):
        self.current_seconds = time.monotonic()
        self.delta_time = round(self.current_seconds - self.previous_seconds, 3)
        self.previous_seconds = self.current_seconds
