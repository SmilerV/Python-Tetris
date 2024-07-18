import time
import pygame as pg
import random

def convert(relative, useold=False):
    if useold:
        return (relative[0]+lx,relative[1]+ly)
    return (relative[0]+x,relative[1]+y)

class Block:
    def __init__(self,blocktype):
        self.blocktype = blocktype
        self.oldrotation = 0
        self.rotation = 0
        self.tiles = Blocks[blocktype][0]
    def rotate(self,rotation=None):
        if type(rotation) != int:
            rotation = None
        if rotation == None:
            rotation = (self.rotation + 1)%4
        self.tiles = Blocks[self.blocktype][rotation]
        
        if self.collides():
            self.tiles = Blocks[self.blocktype][self.rotation]
        else:
            self.rotation = rotation

    def tick(self):
        self.draw()
        self.oldrotation = self.rotation
    def collides(self):
        for i in self.tiles:
            cx, cy = convert(i)
            if cx >= size[0] or cx < 0 or cy >= size[1] or cy < 0 or bg[cx][cy]:
                return True
        return False

    def place(self):
        for i in self.tiles:
            cx, cy = convert(i)
            bg[cx][cy] = True
        print(bg)
    def draw(self):
        for i in Blocks[self.blocktype][self.oldrotation]:
            draw(*convert(i, True), "black")
        for i in self.tiles:
            draw(*convert(i))

#colour data bank
colours = {"blue": [0, 0, 255], "red": [255, 0, 0], "yellow": [0, 255, 0], "green": [255, 0, 255],
           "violet": [255, 255, 0], "orange": [0, 255, 255], "white": [255, 255, 255], "black": [0, 0, 0]}
colors = colours

#block
#rot = rotation
Blocks = {
    'T': [[(0, 0), (-1, 0), (1, 0), (0, -1)],[(0, 0), (1, 0), (0, 1), (0, -1)],[(0, 0), (1, 0), (-1, 0), (0, 1)],[(0, 0), (0, 1), (-1, 0), (0, -1)]],
    'cube': [[(0, 0), (0, -1), (1, 0), (1, -1)],[(0, 0), (0, -1), (1, 0), (1, -1)],[(0, 0), (0, -1), (1, 0), (1, -1)],[(0, 0), (0, -1), (1, 0), (1, -1)]],
    'J': [[(0, 0), (0, 1), (0, -1), (-1,1)],[(0, 0), (-1, -1), (-1, 0), (1, 0)],[(0, 0), (0, 1), (0, -1), (1, -1)],[(0, 0), (-1, 0), (1,0 ), (1, 1)],],
    'L': [[(0, 0), (0, 1), (1, 1), (0, -1)],[(0, 0), (1, 0), (-1, 0), (-1, -1)],[(0, 0), (0, 1), (0, -1), (-1, 1)],[(0, 0), (1, 1), (-1, 0), (1, 0)]],
    'I': [[(0, 0), (0, 1), (0, -1), (0, -2)],[(0, 0), (1, 0), (-1, 0), (-2, 0)],[(0, 0), (0, 1), (0, -1), (0, -2)],[(0, 0), (1, 0), (-1, 0), (-2, 0)],],
    'Z'  : [[(0, 0), (1, 0), (1, -1), (0, 1)],[(0, 0), (-1, 0), (1, 1), (0, 1)],[(0, 0), (1, 0), (1, -1), (0, 1)],[(0, 0), (-1, 0), (1, 1), (0, 1)]],
    'S': [[(0, 0), (0, -1), (1, 1), (1, 0)],[(0, 0), (1, 0), (-1, 1), (0, 1)],[(0, 0), (0, -1), (1, 1), (1, 0)],[(0, 0), (1, 0), (-1, 1), (0, 1)],],
}
blocktypes = ["T","cube","J","L","I","Z","S"]



def draw(x, y, color="blue"):
    pg.draw.rect(surface, colours[color], pg.Rect(x * 50 + 2, y * 50 + 2, 50 - 2, 50 - 2))

changed = True
def update():
    drawBG()
    block.tick()
    pg.display.flip()

def drawBG():
    i=0
    while i <= size[0]:
        i2 = 0
        while i2 <= size[1]:
            if bg[i][i2]:
                draw(i,i2)
            i2 += 1
        i += 1

y = 1
x = 5
lx = 0
ly = 0

down_speed = 2
pg.init()
size = (10,16)
surface = pg.display.set_mode((size[0]*50, size[1]*50))
lastgravity = 0
i = 0
bg = []
temp = []
while i <= size[1]:
    temp.append(False)
    i += 1
i = 0
while i <= size[0]:
    bg.append(temp.copy())
    i += 1
block = Block("J")
while True:
    if time.time()-lastgravity > 1/down_speed:
        y += 1
        if block.collides():
            y -= 1
            block.place()
            y = 1
            x = 5
            block = Block(blocktypes[random.randint(0,6)])
        lastgravity = time.time()
    event = pg.event.get(pg.KEYDOWN)
    if event:
        if event[0].key == pg.K_RIGHT:
            x += 1
            if block.collides():
                x -= 1
        elif event[0].key == pg.K_LEFT:
            x -= 1
            if block.collides():
                x += 1
        elif event[0].key == pg.K_DOWN:
            lastgravity = 0
        elif event[0].key == pg.K_UP:
            block.rotate()
    update()
    lx = x
    ly = y
    time.sleep(0.05)
    event = pg.event.get(pg.WINDOWCLOSE)
    if event:
        break

# Exit program
pg.quit()
