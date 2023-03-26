import random
from random import randint
import pygame as pg
import sys
from car import Car
from grass import Grass
from bar import Bar
from road import Road
def bar_spawn(bar_sprites, i):
    coord = [200, 250, 300, 350] 
    random.shuffle(coord)
    for i in range(3):
        b = Bar(bar, sc, coord[i], 50)
        bar_sprites.append(b)

FPS = 60
W = 800

H = 1000
WHITE = (255, 255, 255)
bar = ('bar.png')

sc = pg.display.set_mode((W, H))
clock = pg.time.Clock() 
# координата x будет случайна
car = Car('car.png', sc)
grass1 = Grass('grass.png', sc, (W - 200)
               // 2, 0)
grass2 = Grass('grass.png', sc, (W - 200) // 2, - H)
road2 = Road('road.png', sc, (W - 200) // 2, - H)
road1 = Grass('road.png', sc, (W - 200)// 2, 0)
bar_sprites = []
coord = [200, 300, 400, 500] 
for i in range(3):
    random.shuffle(coord)
    b = Bar(bar, sc, coord[i], 50)
    bar_sprites
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    grass1.update()
    grass2.update()
    car.update()
    road1.update()
    road2.update()
    for i in range(len(bar_sprites)):
        bar_sprites[i].update()
        if bar_sprites[i].rect.y > H:
            bar_sprites1.clear()
            bar_spawn(bar_sprites1, 0)
                      
        
    grass1.draw()
    grass2.draw()
    car.draw()
    road1.draw()
    road2.draaw()
    pg.display.flip
    clock.tick(FPS)
    pg.display.update()
