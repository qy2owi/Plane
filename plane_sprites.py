'''
@Author: qy2owi
@Date: 2020-05-22 23:21:58
@LastEditTime: 2020-06-08 00:59:55
@Description: file content
'''
# pylint: disable = no-member
import random
import pygame

# 敌机定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 定义屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,480,700)
# 定义屏幕刷新帧率常量
FRAME_PER_SEC = 60


class GameSprite(pygame.sprite.Sprite):
    """游戏精灵基类"""
    
    def __init__ (self, image_name, speed = 1):
    
        # 调用父类初始化方法
        super().__init__()

        # 加载图像
        self.image = pygame.image.load(image_name)
        
        # 设置尺寸
        self.rect = self.image.get_rect()

        # 记录速度
        self.speed = speed

    # 对所有传入的对象进行更新
    def update(self,*args):

        # 飞机默认在垂直方向飞行
        self.rect.y += self.speed

class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self,is_alt=False):

        # 调用父类方法 引用背景图片
        super().__init__("./images/background.png")

        # 判断是否交替图片，如果是，将图片设置到屏幕顶部
        if is_alt:
            self.rect.y = -self.rect.height


    def update(self):

        # 调用父类方法实现更新
        super().update()
        
       # 判断是否移出屏幕，如果移出屏幕，则将图像设置在屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
           self.rect.y = -self.rect.height

           
class Enemy (GameSprite):
    def __init__(self):

        # 调用父类方法 创建敌机精灵 并且导入敌机精灵图片
        super().__init__("./images/Enemy1.png")

        # 设置敌机初始速度
        self.speed = random.randint(1,3)

        # 设置敌机初始出现位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width

        self.rect.x = random.randint(0,max_x)

    def update(self):

        # 调用父类方法 让其垂直运动
        super().update()

        # 判断敌机是否已经飞出屏幕

        if self.rect.y >= SCREEN_RECT.height:
            print ("敌机已经飞出屏幕")
            self.kill()

class Hero(GameSprite):
    def __init__(self):

        # 调用父类方法 创建飞机精灵 并且导入飞机图片
        super().__init__("./images/me1.png",0)

        
        # 设置飞机初始出现位置
        self.rect.centerx = SCREEN_RECT.centerx
        print (self.rect.centerx)
        self.rect.bottom = SCREEN_RECT.bottom - 80


    def update(self):

        self.rect.x += self.speed

        # 判断是否飞出边界
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right





