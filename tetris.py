import time
import pygame as pg
import random
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion
import os
import string
import sys

def obfu(bytes):
    c = 0
    if len(bytes) % 2 == 1:
        c = bytes[len(bytes)-1]
    for i in bytes:
        c = c^i
    r = b""
    for i in bytes:
        r += (c^i).to_bytes()
    return r


def convert(relative, useold=False):
    if useold:
        return (relative[0]+lx,relative[1]+ly)
    return (relative[0]+x,relative[1]+y)

class Block:
    def __init__(self,blocktype, color=None):
        if not color:
            color = Blocks[blocktype][4]
        self.blocktype = blocktype
        self.oldrotation = 0
        self.rotation = 0
        self.color = color
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
            bg[cx][cy] = self.color
    def draw(self, color=None):
        if not color:
            color = self.color
        for i in Blocks[self.blocktype][self.oldrotation]:
            draw(*convert(i, True), "black")
        for i in self.tiles:
            draw(*convert(i), color)

#colour data bank
colours = {"blue": [0, 0, 255], "red": [255, 0, 0], "yellow": [0, 255, 0], "green": [255, 0, 255],
           "violet": [255, 255, 0], "cyan": [0, 255, 255], "white": [255, 255, 255], "black": [0, 0, 0],"orange":[255,153,0],"dark_green":[0,153,0],"purple":[153, 0, 153],"mint":[102, 153, 153],"pink":[255, 102, 204]}
           "violet": [255, 255, 0], "cyan": [0, 255, 255], "white": [255, 255, 255], "black": [0, 0, 0],"orange":[255,153,0],"dark_green":[0,153,0],
           "purple":[153, 0, 153],"mint":[102, 153, 153],"pink":[255, 102, 204],"dark_red":[204, 0, 0]}
colors = colours

#block
Blocks = {

    'T': [[(0, 0), (-1, 0), (1, 0), (0, -1)],[(0, 0), (1, 0), (0, 1), (0, -1)],[(0, 0), (1, 0), (-1, 0), (0, 1)],[(0, 0), (0, 1), (-1, 0), (0, -1)],"violet"],
    'cube': [[(0, 0), (0, -1), (1, 0), (1, -1)],[(0, 0), (0, -1), (1, 0), (1, -1)],[(0, 0), (0, -1), (1, 0), (1, -1)],[(0, 0), (0, -1), (1, 0), (1, -1)],"yellow"],
    'J': [[(0, 0), (0, 1), (0, -1), (-1,1)],[(0, 0), (-1, -1), (-1, 0), (1, 0)],[(0, 0), (0, 1), (0, -1), (1, -1)],[(0, 0), (-1, 0), (1,0 ), (1, 1)],"blue"],
    'L': [[(0, 0), (0, 1), (1, 1), (0, -1)],[(0, 0), (1, 0), (-1, 0), (-1, 1)],[(0, 0), (0, 1), (0, -1), (-1, -1)],[(0, 0), (1, -1), (-1, 0), (1, 0)],"orange"],
    'I': [[(0, 0), (0, 1), (0, -1), (0, -2)],[(0, 0), (1, 0), (-1, 0), (-2, 0)],[(0, 0), (0, 1), (0, -1), (0, -2)],[(0, 0), (1, 0), (-1, 0), (-2, 0)],"cyan"],
    'Z'  : [[(0, 0), (1, 0), (1, -1), (0, 1)],[(0, 0), (-1, 0), (1, 1), (0, 1)],[(0, 0), (1, 0), (1, -1), (0, 1)],[(0, 0), (-1, 0), (1, 1), (0, 1)],"red"],
    'S': [[(0, 0), (0, -1), (1, 1), (1, 0)],[(0, 0), (1, 0), (-1, 1), (0, 1)],[(0, 0), (0, -1), (1, 1), (1, 0)],[(0, 0), (1, 0), (-1, 1), (0, 1)],"green"],

    'C': [[(0, 1), (-1, 0), (-1, -1), (-1, 1),(0, -1)],[(0, 0), (-1, 0), (1, 1), (1, 0),(-1, 1)],[(0, 1), (0, -1), (1, 1), (1, 0),(1, -1)],[(0, 1), (-1, 0), (1, 1), (1, 0),(-1, 1)],[("white")]],
    'O':[[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)],[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)],[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)],[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)],[("dark_green")]],
    'square':[[(0,0),(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)],[(0,0),(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)],[(0,0),(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)],[(0,0),(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)],[("purple")]],
    'i':[[(0,0),(0,-1),(0,1)],[(0,0),(-1,0),(1,0)],[(0,0),(0,-1),(0,1)],[(0,0),(-1,0),(1,0)],[("mint")]],
    'stair':[[(0, 0), (1, 0), (1, -1), (1, 1),(0, 1),(-1,1)],[(0, 0), (-1, 0), (0, 1), (1, 1),(-1, -1),(-1,1)],[(0,-1),(0, 0), (-1,0), (-1, 1), (-1, 1),(1, -1),(-1,-1)],[(0, 0), (1, 1), (1, 0), (0, -1),(1, -1),(-1,-1)],[("pink")]],
    '+':[[(0,0),(0,-1),(0,1),(1,0),(-1,0)],[(0,0),(0,-1),(0,1),(1,0),(-1,0)],[(0,0),(0,-1),(0,1),(1,0),(-1,0)],[(0,0),(0,-1),(0,1),(1,0),(-1,0)],[("dark_red")]],

    'C': [[(0, 1), (-1, 0), (-1, -1), (-1, 1),(0, -1)],[(0, 0), (-1, 0), (1, 1), (1, 0),(-1, 1)],[(0, 1), (0, -1), (1, 1), (1, 0),(1, -1)],[(0, 1), (-1, 0), (1, 1), (1, 0),(-1, 1)],"white"],
    'O':[[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)],[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)],[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)],[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)],"dark_green"],
    'square':[[(0,0),(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)],[(0,0),(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)],[(0,0),(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)],[(0,0),(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)],"purple"],
    'i':[[(0,0),(0,-1),(0,1)],[(0,0),(-1,0),(1,0)],[(0,0),(0,-1),(0,1)],[(0,0),(-1,0),(1,0)],"mint"],
    'stair':[[(0, 0), (1, 0), (1, -1), (1, 1),(0, 1),(-1,1)],[(0, 0), (-1, 0), (0, 1), (1, 1),(-1, -1),(-1,1)],[(0,-1),(0, 0), (-1,0), (-1, 1), (-1, 1),(1, -1),(-1,-1)],[(0, 0), (1, 1), (1, 0), (0, -1),(1, -1),(-1,-1)],"pink"]
}

blocktypes = ["T","cube","J","L","I","Z","S","C","O","square","i","stair"]
if askquestion("Select mode", "Do you want to use extra pieces?") == "no":
    blocktypes.remove("C")
    blocktypes.remove("O")
    blocktypes.remove("square")
    blocktypes.remove("i")
    blocktypes.remove("stair")

    print(blocktypes)


def draw(x, y, color="blue"):
    pg.draw.rect(surface, colours[color], pg.Rect(x * 50 + 2, y * 50 + 2, 50 - 2, 50 - 2))

changed = True
def update():
    drawBG()
    block.tick()
    pg.display.flip()

def lineclear():
    colornames = ["red","yellow","green"]
    i=0
    i0=0
    clears = 0
    while i < size[1]:
        i0+=1
        lineclear = True
        i2 = 0
        while i2 < size[0]:
            i0+=1
            #draw(i2,i,colornames[i0%3])
            lineclear = lineclear and bg[i2][i]
            i2 += 1
        if lineclear:
            clears += 1
            i2 = 0
            while i2 < size[0]:
                bg[i2].pop(i)
                draw(i2,i,"black")
                i2 += 1
            i2 = 0
            while i2 < size[0]:
                bg[i2].insert(0,None)
                i2 += 1
        i += 1
    if clears > 0:
        for i in range(0,size[0]):
            for i2 in range(0,size[1]):
                draw(i,i2,"black")
    return clears

def drawBG():
    i=0
    while i <= size[0]:
        i2 = 0
        while i2 <= size[1]:
            if bg[i][i2]:
                draw(i,i2,bg[i][i2])
            i2 += 1
        i += 1

def highscore(score=None):
    folder = os.environ.get("appdata") + r"\python-tetris\\"
    fn = "highscore.dat"
    if not os.path.exists(folder):
        os.makedirs(folder)
    if not os.path.exists(folder+fn):
        with open(folder+fn,"w") as file:
            file.write("0")
    with open(folder+fn,"rb") as file:
        try:
            cscore = obfu(file.read()).decode()
        except UnicodeDecodeError:
            cscore = "0"
        r = ""
        check = 0
        for i in cscore:
            if i in string.digits:
                r += i
            else:
                check += 1
        cscore = int(r)
        if (cscore*1789)%2801 != check:
            cscore = 0
    newscore = False
    if score:
        if score > cscore:
            newscore = True
            cscore = score
            score = list(str(score))
            with open(folder+fn,"wb") as file:
                fillers = list(string.ascii_letters+"^°´`*+~'#-_.:,;µ|<>@!\"§$%&/()={[]}\\ß?öÖüÜäÄ\t\n\r ²³")
                for _ in range((cscore*1789)%2801):
                    score.insert(random.randint(0, len(score)-1), random.choice(fillers))
                r = ""
                for i in score:
                    r += i
                file.write(obfu(r.encode()))
    return cscore, newscore

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
    temp.append(None)
    i += 1
i = 0
while i <= size[0]:
    bg.append(temp.copy())
    i += 1
temp = None
points = 0
block = Block("J")
while True:
    if time.time()-lastgravity > 1/down_speed:
        y += 1
        if block.collides():
            if y < 3:
                r = str(points)+" Points"
                highscore, new = highscore(points)
                if new:
                    r = "New highscore!\n"+r
                else:
                    r = f"Your highscore: {str(highscore)}\n{r}"
                showinfo("You lost", r)
                break
            y -= 1
            block.place()
            points += lineclear()**2*10
            down_speed = (points / 100).__floor__() + 2
            y = 1
            x = 5
            block = Block(blocktypes[random.randint(0,len(blocktypes)-1)])
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
sys.exit()