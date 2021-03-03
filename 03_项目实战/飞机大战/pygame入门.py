# 李禄波
# 2021/1/29 下午3:48

import pygame
from plane_sprites import *

pygame.init()

# 游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1）加载图像数据
bg = pygame.image.load("./images/background.png")
# 2）绘制图像
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
# screen.blit(hero, (200, 500))
# 英雄飞机所在的初始位置
hero_rect = pygame.Rect(102, 126, 120, 125)

# 在完成所有 blit() 方法完成后统一调用 update()
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 创建敌机的精灵
enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png", 2)

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group((enemy1, enemy2))

# 游戏循环(意味着游戏的正式开始)
while True:

    # 指定循环体内部代码执行的帧率
    clock.tick(60)

    # 监听事件
    for event in pygame.event.get():

        # 退出游戏
        if event.type == pygame.QUIT:
            print("游戏退出")
            pygame.quit()
            exit()

    # 修改飞机的位置
    hero_rect.y -= 1

    # 使飞机循环出现
    if hero_rect.y == -126:
        hero_rect.y = 700

    # 调用blit()方法重新绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 精灵组调用方法
    # update() 让组中的所有精灵调用update()方法
    enemy_group.update()
    # draw() 将精灵全部绘制到指定屏幕上
    enemy_group.draw(screen)

    # 调用update()方法更新显示
    pygame.display.update()


pygame.quit()