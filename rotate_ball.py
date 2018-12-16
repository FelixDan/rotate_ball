# 旋转的球
# 本方法只适用于原地旋转（2018.12.3更新：运动中旋转开发成功）
# 2018.12.12 开始开发多个球围绕一个运动中的球进行旋转
# 2018.12.14 小球围绕大球旋转实现
import random, math
import pygame
from pygame.sprite import Sprite, Group
from pygame.locals import *

class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getx(self): return self.__x
    def setx(self, x): self.__x = x
    x = property(getx, setx)

    def gety(self): return self.__y
    def sety(self, y): self.__y = y
    y = property(gety, sety)

pygame.init()
screen_width, screen_height = 900, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("旋转功能实现")

ball_image = "ball.gif"
littleball_image = "small_ball.gif"


class Ball(Sprite):
    ''' ball class '''
    def __init__(self, image):
        super().__init__()
        self.rawimage = pygame.image.load(image) # 原始图像
        self.image = self.rawimage   # 为旋转后的图像赋初始值
        self.rect = self.rawimage.get_rect()
        self.rect.x = random.randint(100, 800)
        self.rect.y = random.randint(100, 500)
        self.cx = random.randint(100, 800)
        self.cy = random.randint(100, 500)
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

class LittleBall(Ball):
    # 卫星类
    def __init__(self, image, bigball):
        super().__init__(image)
        self.image = image
        self.radius = 60 # 小球旋转半径
        self.angle = random.randint(0, 360) # 小球初始角度
        self.position = Point(0,0) # 小球当前当前圆心（中心）
        self.last_position = Point(0,0) # 上一圆心（中心）
        self.bigball = bigball
   
    def wrap_angle(self, angle):
        return angle % 360
    
    def get_point(self):
        self.angle = self.wrap_angle(self.angle - 2)
        # radians:把角度x转换成弧度
        # sin:求x(x为弧度)的正弦值
        # cos:求x(x为弧度)的余弦值
        self.position.x = math.sin(math.radians(self.angle)) * self.radius
        self.position.y = math.cos(math.radians(self.angle)) * self.radius

        '''

        delta_x = (self.position.x - self.last_position.x)
        delta_y = (self.position.y - self.last_position.y)

        rangle = math.atan2(delta_y, delta_x)
        # degrees:把x从弧度转换成角度
        rangled = self.wrap_angle(-math.degrees(rangle))

        littleball_rotate = pygame.transform.rotate(littleball, rangled)
        '''

    def move(self):
        #littleball_rotate_rect = littleball_rotate.get_rect()
        

        #width1,height1 = littleball_rotate.get_size()
        #screen.blit(littleball_rotate, (279 + position.x - width1//2, 237.5 + position.y - height1//2))
        
        
        self.rect.centerx = self.bigball.cx + self.position.x
        self.rect.centery = self.bigball.cy + self.position.y

        #screen.blit(littleball_rotate, littleball_rotate_rect)

        self.last_position.x = self.position.x
        self.last_position.y = self.position.y

    def update(self):
        self.rotate()
        self.get_point()
        self.move()
        screen.blit(self.image, self.rect)

group = Group()

for i in range(2):
    ball = Ball(ball_image)
    littleball = LittleBall(littleball_image, ball)
    littleball2 = LittleBall(littleball_image, ball)
    group.add(ball, littleball, littleball2)

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
    group.update()
    pygame.display.update()
    
    clock.tick(60) # 帧率
pygame.quit()
