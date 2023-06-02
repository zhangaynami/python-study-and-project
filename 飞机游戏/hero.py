# -*- codeing = utf-8 -*-
import pygame
hero_rect = pygame.Rect(100,500,120,125) #创建矩形对象
print("英雄的原点%d %d"%(hero_rect.x,hero_rect.y)) #位置
print("英雄的尺寸%d %d"%(hero_rect.width,hero_rect.height)) #大小
print(hero_rect.size)