import sys
import pygame
from settings import Settings
from ship import Ship,Character
import game_functions as gf
from pygame.sprite import Group
def run_game():

    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(ai_settings,screen)
    bullets = Group()
    character = Character(screen)
    pygame.display.set_caption("alien invasion")
    # bg_color = (230,230,230)

    while True:

        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets,ai_settings)
        gf.update_screen(ai_settings,screen,ship,character,bullets)

run_game()
