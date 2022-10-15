import pygame as pg
import sys
import time
from pygame.locals import *


pg.init()
width = 600
height = 600
black = (0,0,0)
fps = 60
CLOCK = pg.time.Clock()
pg.time.get_ticks()
window = pg.display.set_mode((width, height),0,fps)
pg.display.set_caption("TIC TAC TOE")
x_img = pg.image.load("tttO.png")
y_img = pg.image.load("tttx.png")
x_img = pg.transform.scale(x_img,(200,200))
y_img = pg.transform.scale(y_img,(200,200))

