import pygame,sys
pygame.init()
win=pygame.display.set_mode([1002,980])
win.fill([255,255,255])
cimo=pygame.image.load('1.png')
win.blit(cimo,[50,50])
pygame.display.flip()
runling=True
while runling:
    for lise in pygame.event.get():
        if lise.type==pygame.QUIT:
            runling=False
pygame.quit()
