from Physics import Physics
from Window import Window
from Event import Event
from Player import Player
from Platform import Platform
from Sprite import Sprite
from common import COLORS

class Game:
    def __init__(self):
        self.quit = False

        self.physics = Physics(self)
        self.window = Window(self, COLORS.WHITE)
        self.event = Event(self)
        self.player = Player(self, COLORS.BLACK, 0, 0, 50, 50, 2500)
        self.platform = Platform(self, COLORS.GREEN, 200, 700, 400, 10, 0)
        self.sprite = Sprite(self)

        self.sprite.all_sprites.add(self.player, self.platform)
        self.sprite.gravity_sprites.add(self.player)
        self.sprite.platform_sprites.add(self.platform)

        self.update_queue = [
            self.window.update_background,
            self.sprite.update_sprites,
            self.physics.update_gravity,
            self.event.update_event,
            self.window.update_window,
            self.physics.update_delta_time
        ]

    def start(self):
        while not self.quit:
            for update in self.update_queue:
                update()
