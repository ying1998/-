import sys
import pygame
from settings import Settings
from event_key import Event_key
import game_functions as gf


def run_game():

    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    printevent_key = Event_key(ai_settings,screen)

    pygame.display.set_caption("event key")

    while True:
        gf.check_events(printevent_key)
        #printevent_key.update()
        gf.update_screen(ai_settings,screen,printevent_key)

run_game()
