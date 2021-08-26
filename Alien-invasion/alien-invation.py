import pygame
from ship import Ship
import game_functions as gf
from settings import Settings
from pygame.sprite import Group


def run_Game():
    # 初始化屏幕并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_Width, ai_settings.screen_Height))
    pygame.display.set_caption("Alien Invation")

    # 创建一艘飞船
    ship = Ship(screen, ai_settings)

    # 创建子弹
    bullets = Group()

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # 每次循环更新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)



run_Game()
