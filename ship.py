import pygame
import setting


class Ship():

    def __init__(self, screen):
        # 初始化飞船并设置其初始位置
        self.screen = screen

        # 加载飞船图像，并获取其矩形
        self.image = pygame.image.load(setting.IMAGE_DIR)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 把飞船初始放在中间位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    # 在指定位置绘制飞船
    def blitme(self):
        self.screen.blit(self.image, self.rect)
