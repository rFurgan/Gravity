import pygame
from common import DIRECTION

class Player(pygame.sprite.Sprite):
    def __init__(self, game, color, x, y, width, height, accelaration):
        super().__init__()
        self.game = game
        self.accelaration = accelaration

        self.image = pygame.Surface([width, height])
        self.image.fill(color.value)
        pygame.draw.rect(self.image, color.value, pygame.Rect(x, y, width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, direction):
        if (direction == DIRECTION.UP):
            self.rect.y -= self.get_distance(self.game.physics.delta_time)
        elif (direction == DIRECTION.DOWN):
            self.rect.y += self.get_distance(self.game.physics.delta_time)
        elif (direction == DIRECTION.LEFT):
            self.rect.x -= self.get_distance(self.game.physics.delta_time)
        elif (direction == DIRECTION.RIGHT):
            self.rect.x += self.get_distance(self.game.physics.delta_time)

        else:
            pass

    def get_speed(self, delta_time):
        return self.accelaration * delta_time

    def get_distance(self, delta_time):
        return self.get_speed(delta_time) * delta_time
