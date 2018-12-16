import random
import pygame
from pygame.sprite import Sprite


class Big_Ball(Sprite):
    ''' ball class '''
    def __init__(self, screen, image):
        super().__init__()
        self.screen = screen
        self.rawimage = pygame.image.load(image) # 原始图像
        self.image = self.rawimage   # 为旋转后的图像赋初始值
        self.rect = self.rawimage.get_rect()
        self.rect.x = random.randint(100, 800)
        self.rect.y = random.randint(100, 500)
        self.cx = random.randint(100, 800)
        self.cy = random.randint(100, 500)
        self.x_speed = 5
        self.y_speed = 5
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
        '''前进和碰撞边缘检测'''
        #self.rect.move_ip(self.vx, self.vy) # move_ip()可以移动目标，横向、纵向距离为x,y
        self.rect.centerx = self.cx
        self.rect.centery = self.cy

        if self.rect.right >= self.screen.get_width():
            self.x_speed = -abs(self.x_speed)
        if self.rect.left <= 0:
            self.x_speed = abs(self.x_speed)        
        if self.rect.bottom >= self.screen.get_height():
            self.y_speed = -abs(self.y_speed)
        if self.rect.top <=0:
            self.y_speed = abs(self.y_speed)

        self.cx += self.x_speed
        self.cy += self.y_speed


    def update(self):
        self.rotate()
        self.move()
        self.screen.blit(self.image, self.rect)