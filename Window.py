import pygame
from common import COLORS

FPS = 60
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

class Window:
    def __init__(self, game, background_color):
        pygame.init()
        self.game = game
        self.background_color = background_color
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

    def update_window(self):
        pygame.display.update()
        self.clock.tick(FPS)

    def update_background(self):
        self.window.fill(self.background_color.value)
