import sys
import pygame
from settings import Settings
from rocket import Rocket
import game_functions as gf


def run_game():

    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    rocket = Rocket(ai_settings,screen)

    pygame.display.set_caption("rocket movement")
    # bg_color = (230,230,230)

    while True:

        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(ai_settings,screen,rocket)

run_game()
