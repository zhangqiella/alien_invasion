import pygame
import sys
import setting


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                ship.rect.centerx -= 1
            elif event.type == pygame.K_RIGHT:
                ship.rect.centerx += 1



def update_screen(screen, ship):
    screen.fill(setting.bg_color)
    # 让最近绘制的屏幕可见

    ship.blitme()
    pygame.display.flip()
