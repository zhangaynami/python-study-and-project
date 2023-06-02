# -*- codeing = utf-8 -*-
import pygame
from plane_sprites import *
pygame.quit()
#创建游戏窗口
screen = pygame.display.set_mode((480,700))
#绘制背景图像
bg = pygame.image.load("./images/background.png") #加载图像
screen.blit(bg,(0,0)) #绘制图像
#英雄的飞机
hero = pygame.image.load("./images/me1.png")

pygame.display.update()
#游戏循环，游戏正式开始
clock = pygame.time.Clock()

hero_rect = pygame.Rect(150,300,102,126)
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",2)
enemy_group = pygame.sprite.Group(enemy,enemy1)

while True:
    clock.tick(60)
    #捕获事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出")
            pygame.quit()
            exit()

    hero_rect.y -= 2
    if hero_rect.y == -126:
        hero_rect.y = 700

    screen.blit(bg, (0, 0))
    screen.blit(hero,hero_rect)

    enemy_group.update()#让组中所有精灵捕获位置
    enemy_group.draw(screen) #绘制所有精灵
    pygame.display.update()

pygame.quit()