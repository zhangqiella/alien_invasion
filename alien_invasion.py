import sys
import pygame
import setting
from ship import Ship
import game_function as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 这里定义的Settings要实例化
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = setting.bg_color

    ship = Ship(screen)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship)
        gf.update_screen(screen, ship)


if __name__ == '__main__':
    run_game()
