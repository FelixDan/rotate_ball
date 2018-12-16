import random, math
from big_ball import Ball
from point import Point

class Middle_Ball(Ball):
    # 卫星类
    def __init__(self, screen, image, bigball):
        super().__init__(screen, image)
        self.screen = screen
        self.image = image
        self.bigball = bigball
        self.radius = 60 # 小球旋转半径
        self.angle = random.randint(0, 360) # 小球初始角度
        self.position = Point(0,0) # 小球当前当前圆心（中心）
        self.last_position = Point(0,0) # 上一圆心（中心）
        
   
    def wrap_angle(self, angle):
        return angle % 360
    
    def get_point(self):
        self.angle = self.wrap_angle(self.angle - 2)
        # radians:把角度x转换成弧度
        # sin:求x(x为弧度)的正弦值
        # cos:求x(x为弧度)的余弦值
        self.position.x = math.sin(math.radians(self.angle)) * self.radius
        self.position.y = math.cos(math.radians(self.angle)) * self.radius


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
        self.screen.blit(self.image, self.rect)