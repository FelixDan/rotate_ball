# 旋转的球
# 本方法只适用于原地旋转（2018.12.3更新：运动中旋转开发成功）
# 2018.12.12 开始开发多个球围绕一个运动中的球进行旋转
# 2018.12.14 小球围绕大球旋转实现
import random
import pygame
from pygame.sprite import Sprite, Group
from pygame.locals import *

from big_ball import Ball
from middle_ball import Middle_Ball

pygame.init()
screen_width, screen_height = 900, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("旋转功能实现")

ball_image = "ball.gif"
middleball_image = "small_ball.gif"
little_ball_image = "check-icon16.png"



group = Group()

for i in range(2):
    ball = Ball(screen, ball_image)
    middleball = Middle_Ball(screen, middleball_image, ball)
    middleball2 = Middle_Ball(screen, little_ball_image, ball)

    group.add(ball, middleball, middleball2)

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
