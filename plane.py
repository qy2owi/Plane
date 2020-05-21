# 解决误报module 中无此参数的问题
 # pylint: disable=no-member

import pygame

pygame.init()

# 创建游戏窗口 
screen = pygame.display.set_mode((400,700))

# 绘制背景图像
# >1.加载图像数据 
bg = pygame.image.load("./images/background.png")

# 绘制飞机位置
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(150,500))


# 所有对象绘制完成后，统一调用update方法刷新界面
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义Rect 记录飞机初始位置
hero_rect = pygame.Rect(150,500,102,126)


while True:
    #　设置帧率为60 
    clock.tick(60)

    # 修改飞机位置
    hero_rect.y -= 1

    # 实现飞机循环飞行
    if hero_rect.bottom <= 0:
        hero_rect.y = 700

    # 监听事件
    for event in pygame.event.get():

        # 监听游戏退出事件
        if event.type == pygame.QUIT:

            print("退出游戏")
            # quit 卸载所有模块
            pygame.quit()
            # 终止当前执行的程序
            exit()

    #调用 blit 方法绘制图像
    #　背景图像
    screen.blit(bg,(0,0))
    # 飞机图像
    screen.blit(hero,hero_rect)
    # 调用方法刷新图像
    pygame.display.update()