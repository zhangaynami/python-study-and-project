# -*- codeing = utf-8 -*-
import pygame.sprite
#定义屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,480,700)
#刷新的帧率
FRAME_PER_SEC = 60
class GameSprite(pygame.sprite.Sprite):
    """
    飞机大战精灵
    """
    def __init__(self,image_name,speed = 1):
        super().__init__()
        #确定对象属性
        self.image = pygame.image.load(image_name) # 加载对象位置
        self.rect = self.image.get_rect() #加载图像位置
        self.speed = speed #加载图像速度
    def update(self):
        self.rect.y += self.speed

class Backgroud(GameSprite):
    """游戏背景精灵"""
    def __init__(self,is_alt = False):
        #调用父类
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        #   调用父类的方法实现
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
        pass