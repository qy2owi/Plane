'''
@Author: qy2owi
@Date: 2020-05-21 11:37:48
@LastEditTime: 2020-06-09 21:04:38
@Description: file content
'''
#导入模块
# pylint: disable = no-member

import pygame

from plane_sprites import *

class PlaneGame(object):

    # 游戏初始化
    def __init__(self):
        print("游戏初始化")
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        # 设置定时器事件 第一个值为事件ID 第二个值为事件触发间隔的毫秒值
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        # 设置发射子弹的定时器， 每0.5 发射一次子弹
        pygame.time.set_timer(HERO_FIRE_EVENT,500)


    def __create_sprites(self):
        """创建精灵组"""

        # 背景组
        bg1 = Background()
        bg2 = Background(True)
        
        self.back_group = pygame.sprite.Group(bg1,bg2)

        # 敌机组
        self.enemy_group = pygame.sprite.Group()

        # 英雄组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    def start_game(self):
        print("游戏开始")

        while True:
            # 设置时钟刷新率
            self.clock.tick(FRAME_PER_SEC)
            # 事假监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新精灵组
            self.__update_sprites()
            # 更新屏幕检测
            pygame.display.update()

    def __event_handler(self):
        """事件监听"""
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                self.enemy_group.add(Enemy())
                print("敌机出现了")
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        # 使用键盘提供的方法获取键盘的值 - 按键元祖
        keys_pressed = pygame.key.get_pressed()

        # 判断元祖中对应的索引值
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0

    def __check_collide(self):
        """碰撞检测"""
        # 1. 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group, True, True)
        # 2. 敌机摧毁战机
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)

        # 销毁战机

        if len(enemies) > 0 : 
            self.hero.kill()

            PlaneGame.__game_over()

    def __update_sprites(self):
        """更新精灵组"""
        for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets]:
            group.update()
            group.draw(self.screen)

    @staticmethod
    def __game_over():
        """游戏结束""" 
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏架构
    game = PlaneGame()

    # 开始游戏
    game.start_game()
    

    
