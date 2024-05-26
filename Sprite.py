from pygame import sprite

class Sprite:
    def __init__(self, game):
        self.game = game
        self.all_sprites = sprite.Group()
        self.gravity_sprites = sprite.Group()
        self.platform_sprites = sprite.Group()

    def update_sprites(self):
        self.all_sprites.update()
        self.all_sprites.draw(self.game.window.window)
