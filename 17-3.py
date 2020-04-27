# -*- coding: utf-8 -*-
print('本程序为谢名轩所写',end=',')
print('邮箱2091549152@qq.com')
import sys,pygame
from random import *
class MyBallClass(pygame.sprite.Sprite):
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
        if self.rect.top <0 or self.rect.bottom>height:
            self.speed[1]=-self.speed[1]
def animate(group):
    win.fill([255,255,255])
    for ball in group:
        ball.move()
    for ball in group:
        group.remove(ball)
        if pygame.sprite.spritecollide(ball,group,False):
            ball.speed[0]=-ball.speed[0]
            ball.speed[1]=-ball.speed[1]
        group.add(ball)
        win.blit(ball.image,ball.rect)
    pygame.display.flip()
    pygame.time.delay(20)
size=width,height=645,485
win=pygame.display.set_mode(size)
pygame.display.set_caption("谢名轩的作品(1,17-3)")
win.fill([255,255,255])
img_file='th.png'
group=pygame.sprite.Group()
for row in range(0,3):
    for column in range(0,3):
        location=[column*180+10,row*180+10]
        speed=[choice([-2,2]),choice([-2,2])]
        ball=MyBallClass(img_file,location,speed)
        group.add(ball)
running=True
while running:
    for inx in pygame.event.get():
        if inx.type==pygame.QUIT:
            running=False
    animate(group)
pygame.quit()