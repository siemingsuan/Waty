import pygame,sys
pygame.init()
win=pygame.display.set_mode([640,480])
win.fill([255,255,255])
ball=pygame.image.load('th.png')
x=50
y=50
xs=5
run=True
while run:
    for castfilllo in pygame.event.get():
        if castfilllo.type==pygame.QUIT:
            run=False
    pygame.time.delay(20)
    pygame.draw.rect(win,[255,255,255],[x,y,90,90],0)
    x=x+xs
    if x>win.get_width():
        x=-90
    win.blit(ball,[x,y])
    pygame.display.flip()
pygame.quit()
