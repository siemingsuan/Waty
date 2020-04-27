import pygame
pygame.init()
fong=pygame.display.set_mode([640,480])
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
pygame.quit()