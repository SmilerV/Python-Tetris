print("Tetris")
import time
import pygame as pg
import random

class Block:
    def __init__(self,blocktype):
        self.x = 5
        self.y = 4
        self.tiles = Blocks[blocktype]
    def rotate(self,rotation=None):
        if type(rotation) == "integer"  

    def draw(self):
        for i in self.tiles:
            draw(*i)

#colour data bank
colours = {"blue": [0, 0, 255], "red": [255, 0, 0], "yellow": [0, 255, 0], "green": [255, 0, 255],
           "violet": [255, 255, 0], "orange": [0, 255, 255], "white": [255, 255, 255], "black": [0, 0, 0]}
colors = colours

#block

Blocks = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'cube': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'downT': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    '_': [(0, 0), (1, 0), (0, -1), (-1, -1)],
    'reverseS'  : [(0, 0), (-1, 0), (-1, -1), (0, 1)],
    'S': [(0, 0), (-1, 0), (-1, 1), (0, -1)]

}
#random block
temp = ["T","cube","J","L","I","downT","_","reverseS","S"]
s=Blocks[temp[random.randint(0,8)]]




def draw(x, y, color="blue"):
    pg.draw.rect(surface, colors[color], pg.Rect(x * 50 + 2, y * 50 + 2, 50 - 2, 50 - 2))

changed = True
def update():
    draw(lx,ly,"black")
    draw(x,y)
    pg.display.flip()

y = 0
x = 0
lx = 0
ly = 0

down_speed = 2
pg.init()
size = (10,16)
surface = pg.display.set_mode((size[0]*50, size[1]*50))
lastgravity = 0
while True:
    if time.time()-lastgravity > 1/down_speed:
        y += 1
    event = pg.event.get(pg.KEYDOWN)
    if event:
        if event[0].key == pg.K_RIGHT:
            x += 1
        elif event[0].key == pg.K_DOWN:
            lastgravity = 0
    update()
    lx = x
    ly = y
    event = pg.event.get(pg.WINDOWCLOSE)
    if event:
        break

# Exit program
pg.quit()




