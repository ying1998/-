import pygame


class Rocket():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings
        ## WARNING:
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect  = self.screen.get_rect()
        # postion
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom  = self.screen_rect.centerx

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        # flag move
        self.moving_right = False
        self.moving_left  = False
        self.moving_up    = False
        self.moving_down  = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.rocket_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.rocket_speed_factor
        elif self.moving_up and self.rect.top > 0 :
            self.bottom -=self.ai_settings.rocket_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.rocket_speed_factor

        self.rect.centerx = self.center
        self.rect.bottom  = self.bottom
    def blitme(self):
        self.screen.blit(self.image,self.rect)
