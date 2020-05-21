'''
@Author: qy2owi
@Date: 2020-05-21 11:37:48
@LastEditTime: 2020-05-22 11:08:13
@Description: file content
'''
#设置模块中变量名不报错
# pylint: disable=no-member

import pygame

#初始化界面
pygame.init()

# 创建游戏窗口 480*700
screen = pygame.display.set_mode((480,700))

# 创建背景
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))

# 创建飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (190, 500))

# 定义rect记录飞机初始位置
hero_rect = pygame.Rect(190,500,102,126)

# 创建完了所有对象以后刷新面板 
pygame.display.update()

# 创建时钟参数
clock = pygame.time.Clock()

while True:
    # 设置刷新帧数为60
    clock.tick(60)

    # 设置事件监听
    for event in pygame.event.get():
        
        # 退出事件
        if event.type == pygame.QUIT:

            # 打印相关信息
            print("退出游戏")
            # 关闭所有模块
            pygame.quit()
            # 退出当前脚本
            exit()

    # 移动飞机位置
    hero_rect.y -= 10

    # 使飞机循环飞行
    if hero_rect.bottom <= 0:
        hero_rect.y = 700

    # 绘制改变后的图像
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)

    pygame.display.update()

