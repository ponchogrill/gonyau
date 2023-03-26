import pygame as pg
W = 800
H = 1000
class Grass(pg.sprite.Sprite):
    def __init__(self, filename, screen, x, y):
        self.screen = screen
        pg.sprite.Sprite.__init__(self)
        img = pg.image.load(filename).convert()
        self.image = pg.transform.scale(img,(600,1000))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
    def update(self):
        self.rect.y += 2
        if self.rect.y >= 1000:
            self.rect.y = -1000
    def draw(self):
        self.screen.blit(self.image, self.rect)
