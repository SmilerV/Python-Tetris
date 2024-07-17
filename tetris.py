import time
import pygame as pg
import random

def convert(relative):
    r=[]
    for i in relative:
        r.append((i[0]+x, i[1]+y))
    return r

class Block:
    def __init__(self,blocktype):
        self.x = 5
        self.y = 4
        self.tiles = Blocks[blocktype][0]
    def rotate(self,rotation=None):
        self.oldrotation
        if type(rotation) != int:
            rotation = None
        if rotation == None:
            rotation = self.rotation + 1
        self.tiles = Blocks[self.blocktype][rotation]
        

     
    def draw(self):
        for i in Blocks[self.blocktype][self.oldrotation]:
            draw(*convert(i), "black")
        for i in self.tiles:
            draw(*convert(i))

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
#randomizer
temp = ["T","cube","J","L","I","downT","_","reverseS","S"]
s=Blocks[temp[random.randint(0,8)]]




def draw(x, y, color="blue"):
    pg.draw.rect(surface, colours[color], pg.Rect(x * 50 + 2, y * 50 + 2, 50 - 2, 50 - 2))

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
        lastgravity = time.time()
    event = pg.event.get(pg.KEYDOWN)
    if event:
        if event[0].key == pg.K_RIGHT:
            x += 1
        if event[0].key == pg.K_LEFT:
            x -= 1
        elif event[0].key == pg.K_DOWN:
            lastgravity = 0
    update()
    lx = x
    ly = y
    time.sleep(0.05)
    event = pg.event.get(pg.WINDOWCLOSE)
    if event:
        break

# Exit program
pg.quit()


#line clear

def clear_lines(self):
        for i, row in enumerate(self.grid[:-1]):
            if all(cell != 0 for cell in row):
                lines_cleared += 1
                del self.grid[i]
                self.grid.insert(0, [0 for _ in range(self.width)])
        return lines_cleared

#valid moves

def valid_move(self, piece, x, y, rotation):
        for i, row in enumerate(piece.shape[(piece.rotation + rotation) % len(piece.shape)]):
            for j, cell in enumerate(row):
                try:
                    if cell == 'O' and (self.grid[piece.y + i + y][piece.x + j + x] != 0):
                        return False
                except IndexError:
                    return False
        return True
