# -*- coding: utf-8 -*-
print('本程序为谢名轩所写',end=',')
print('邮箱2091549152@qq.com')
import sys,pygame
from random import *
class Myball(pygame.sprite.Sprite):
    def __init__(self,image_file,location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image_file)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=location
        self.speed=speed
    def move(self):
        self.rect=self.rect.move(self.speed)
        if self.rect.left<0 or self.rect.right>width:
            self.speed[0]=-self.speed[0]
        if self.rect.top<0 or self.rect.bottom>height:
            self.speed[1]=-self.speed[1]
size=width,height=640,480
win=pygame.display.set_mode(size)
win.fill([255,255,255])
image_file='th.png'
balls=[]
for row in range(0,3):
    for column in range(0,3):
        location=[column*180+10,row*180+10]
        speed=[choice([-2,2]),choice([-2,2])]
        ball=Myball(image_file,location,speed)
        balls.append(ball)
running=True
while running:
    for eventi in pygame.event.get():
        if eventi.type==pygame.QUIT:
            running=False
    pygame.time.delay(20)
    win.fill([255,255,255])
    for ball in balls:
        ball.move()
        win.blit(ball.image,ball.rect)
    pygame.display.flip()
pygame.quit()
