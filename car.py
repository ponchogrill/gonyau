import pygame as pg
W = 800
H = 1000
class Car(pg.sprite.Sprite):
    def __init__(self, filename, sc):
        self.screen = sc
        pg.sprite.Sprite.__init__(self)
        img = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(img,(50,80))
        self.rect = self.image.get_rect()
        self.rect.centerx = W // 2
        self.rect.bottom = H - 10
        self.x = 400
        self.speedx=5
    def update(self):
        keys = pg.key.get_pressed()
        self.speedx+=self.x
        #если нажата
        if keys[pg.K_RIGHT]:
            self.speedx+=5
        #если нажата
        if keys[pg.K_LEFT]:
            self.speedx+=-5
    def draw(self):
        self.screen.blit(self.image, self.rect)
            
        
