# 李禄波
# 2021/1/30 下午1:28

import random
import pygame

# 屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 敌机的定时器事件
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    # 重写update()方法
    def update(self):

        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1.调用父类方法实现精灵的创建
        super().__init__("./images/background.png")

        # 2.判断是否是交替图像
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1.调用父类方法
        super().update()

        # 2.判断是否移出屏幕，如果移出了则将其移动到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:

            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):

        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")

        # 2.指定敌机的初始随机速度(1~3)
        self.speed = random.randint(1, 3)

        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0

        # 敌机所能允许出现的最大x值
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        # 1.调用父类方法，保持垂直方向的飞行
        super().update()

        # 2.判断是否飞出屏幕，飞出屏幕则从精灵组中删除精灵
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):

        # 1.调用父类方法设置图像和初始速度
        super(Hero, self).__init__("./images/me1.png", 0)

        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 3.创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):

        # 英雄在水平方向上移动
        self.rect.x += self.speed

        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):

        # 一次发射三枚子弹
        for i in (0, 1, 2):
            # 1.创建子弹精灵
            bullet = Bullet()

            # 2.设置精灵的初始位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            # 3.将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):

        # 1.调用父类方法设置子弹图片
        super(Bullet, self).__init__("./images/bullet1.png", -2)

    def update(self):

        # 1.调用父类方法，让子弹沿垂直方向飞行
        super(Bullet, self).update()

        # 2.删除飞出屏幕的子弹
        if self.rect.bottom < 0:

            self.kill()

    # def __del__(self):
    #
    #     print("子弹完蛋了。。。")

