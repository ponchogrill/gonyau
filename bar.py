import pygame as pg
W = 800
H = 1000
class Bar(pg.sprite.Sprite):
    def __init__(self, filename, screen, x, y):
        self.screen = screen
        pg.sprite.Sprite.__init__(self)
        img = pg.image.load(filename).convert()
        self.image = pg.image.load('bar.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.screen.blit(self.image, self.rect)
