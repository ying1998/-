
class Settings():

    def __init__(self):

        self.screen_width = 1200
        self.screen_height= 800
        self.bg_color     = (230,230,230)
        # ship's settings
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width        = 15 # 3 ->15
        self.bullet_height       = 3  # 15 ->3
        self.bullet_color        = 60,60,60
        self.bullets_allowed     = 5
