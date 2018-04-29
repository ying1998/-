import pygame

class Ship(object):
    """docstring for [object Object]."""
    def __init__(self, ai_settings,screen):

        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/flyship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect  = self.screen.get_rect()
        # postion center is in left
        self.rect.centerx = self.screen_rect.left
        self.rect.bottom  = self.screen_rect.centerx

        #self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        # flag move
        self.moving_up = False
        self.moving_down  = False
    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.bottom -= self.ai_settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor
        self.rect.bottom = self.bottom
    def blitme(self):
        self.screen.blit(self.image,self.rect)

class Character():

    def __init__(self,screen):
        self.screen =screen
        self.image = pygame.image.load('images/character.bmp')
        self.rect =self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image,self.rect)
