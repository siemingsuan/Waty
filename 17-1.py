import sys,pygame
class Myball(pygame.sprite.Sprite):
    def __init__(self,image_file,location):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image_file)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=location
size=width,height=640,480
win=pygame.display.set_mode(size)
win.fill([255,255,255])
img="th.png"
balls=[]
for row in range(0,3):
    for cool in range(0,3):
        location=[cool*180+10,row*180+10]
        ball=Myball(img,location)
        balls.append(ball)
for ball in balls:
    win.blit(ball.image,ball.rect)
pygame.display.flip()
running=True
while running:
    for cast in pygame.event.get():
        if cast.type==pygame.QUIT:
            running=False
pygame.quit()
