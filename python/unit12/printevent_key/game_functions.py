import sys
import pygame

def check_events(printevent_key):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
            print("pygame.KEYDOWN: %s" %event.key)
        elif event.type == pygame.KEYUP:
            print("pygame.KEYUP: %s" %event.key)
def update_screen(ai_settings,screen,printevent_key):
    screen.fill(ai_settings.bg_color)
    #printevent_key.blitme()

    pygame.display.flip()
