import sys
import pygame
from bullet import Bullet

def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
def update_screen(ai_settings,screen,ship,character,bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    character.blitme()
    pygame.display.flip()


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_events(event,ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False



def update_bullets(bullets,ai_settings):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.left >=ai_settings.screen_width :
            bullets.remove(bullet)
    # print(len(bullets))

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets)< ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
