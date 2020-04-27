import pygame,sys
from pygame.color import THECOLORS
pygame.init()
fong=pygame.display.set_mode([640,480])
fong.fill([255,255,255])
pygame.draw.circle(fong,THECOLORS["blue"],[230,240],30,0)
pygame.display.flip()
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
pygame.quit()