import pygame,sys
pygame.init()
awindow=pygame.display.set_mode([640,480])
awindow.fill([255,255,255])
theball=pygame.image.load('th.png')
x=50
y=50
hellox=10
helloy=10
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.time.delay(20)
    pygame.draw.rect(awindow,[255,255,255],[x,y,90,90],0)
    x=x+hellox
    y=y+helloy
    if x>awindow.get_width()-90 or x<0:
        hellox=-hellox
    if y>awindow.get_width()-90 or y<0:
        helloy=-helloy
    awindow.blit(theball,[x,y])
    pygame.display.flip()
pygame.quit()
