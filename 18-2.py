# -*- coding: utf-8 -*-
print('本程序为谢名轩所写',end=',')
print('邮箱2091549152@qq.com')
import sys,pygame
pygame.init()
screen = pygame.display.set_mode([640,480])
pygame.display.set_caption("谢名轩的作品(1,18-1)")
pli = pygame.Surface(screen.get_size())
pli.fill([255,255,255])
clock = pygame.time.Clock()
class Ball(pygame.sprite.Sprite):
    def __init__(self,image_file,speed,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed = speed
    def move(self):
            if self.rect.left <= screen.get_rect().left or self.rect.right >= screen.get_rect().right:
                self.rect.right >= screen.get_rect().right:
                self.speed[0]=-self.speed[0]
            newpos=self.rect.move(self.speed)
            self.rect=newpos
ball = Ball('th.png',[10,0],[20,20])
delay = 100
itv = 50
pygame.key.set_repeat(delay,itv)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball.rect.top = ball.rect.top - 10
            elif event.key == pygame.K_DOWN:
                ball.rect.top = ball.rect.top + 10
    clock.tick(30)
    screen.blit(pli,[0,0])
    ball.move()
    screen.blit(ball.image,ball.rect)
    pygame.display.flip()
pygame.quit()
