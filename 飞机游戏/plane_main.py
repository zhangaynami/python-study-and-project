# -*- codeing = utf-8 -*-
import pygame
from plane_sprites import *

class PlaneGame(object):
    def __init__(self):
        print("游戏初始化")
        #创建窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #创建时钟
        self.clock = pygame.time.Clock()
        #调用私有方法，创建精灵和精灵组
        self.__create_sprities()
    def __create_sprities(self):
        #创建背景和精灵组
        bg1 = Backgroud()
        bg2 = Backgroud(is_alt=True)

        self.back_ground = pygame.sprite.Group(bg1,bg2)

    def start_game(self):
        print("游戏开始")
        while True:
            #设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            #事件监听
            self.__event_handler()
            #碰撞检测
            self.__check_collide()
            #更新绘制精灵
            self.__update_sprites()
            #更新显示

            pygame.display.update()

    def __event_handler(self):
       for event in  pygame.event.get():
           #判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
    def __check_collide(self):
        pass
    def __update_sprites(self):
        self.back_ground.update()
        self.back_ground.draw(self.screen)
    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()

if __name__ == "__main__":
    game = PlaneGame()
    game.start_game()