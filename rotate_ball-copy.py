# 旋转的球
# 本方法只适用于原地旋转（2018.12.3更新：运动中旋转开发成功）
# 2018.12.12 开始开发多个球围绕一个运动中的球进行旋转
import random, math
import pygame
from pygame.sprite import Sprite, Group
from pygame.locals import *

pygame.init()
screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("旋转功能实现")

ball_image = "ball.gif"

class Ball(Sprite):
    ''' ball class '''
    def __init__(self, image):
        super().__init__()
        self.rawimage = pygame.image.load(image) # 原始图像
        self.image = self.rawimage   # 为旋转后的图像赋初始值
        self.rect = self.rawimage.get_rect()
        self.rect.x = random.randint(100, 900)
        self.rect.y = random.randint(100, 700)
        self.cx = random.randint(100, 900)
        self.cy = random.randint(100, 700)
        self.x_spped = 2
        self.y_speed = 2
        self.degrees = 0

    def rotate(self):
        self.degrees += 2
        self.degrees = self.degrees % 360
        self.image = pygame.transform.rotate(self.rawimage, self.degrees)
        self.rect = self.image.get_rect()

        # 下面的坐标是原地旋转的关键
        # 可以在后面加减任意数值以改变旋转位置
        # 下面是居中旋转
        #self.rect.x = (screen_width - self.rect.w) // 2   # + 100
        #self.rect.y = (screen_height - self.rect.h) // 2  # + 200

        # 下面是显示的旋转球的外框，可以对其所在的rect有个直观了解
        #pygame.draw.rect(screen, [255, 255, 255], (self.rect.centerx - 25, self.rect.centery - 25, self.rect.w, self.rect.h), 2)

    def move(self):
        #self.rect.move_ip(self.vx, self.vy) # move_ip()可以移动目标，横向、纵向距离为x,y
        self.rect.centerx = self.cx
        self.rect.centery = self.cy

        if self.rect.right >= screen.get_width():
            self.x_spped = -5
        if self.rect.left <= 0:
            self.x_spped = 5        
        if self.rect.bottom >= screen.get_height():
            self.y_speed = -5
        if self.rect.top <=0:
            self.y_speed = 5

        self.cx += self.x_spped
        self.cy += self.y_speed


    def update(self):
        self.rotate()
        self.move()
        screen.blit(self.image, self.rect)

group = Group()

for i in range(1):
    ball = Ball(ball_image)
    group.add(ball)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            running = False

    screen.fill([230, 230, 230])
    '''
    star.rotate()
    star2.rotate()
    star.move()
    star2.move()
    star.update()
    star2.update()
    '''
    group.update()
    pygame.display.update()
    
    clock.tick(50) # 帧率
pygame.quit()
