import random
import arcade
class R_paddle:
    def __init__(self):
        super().__init__()
        self.color = arcade.color.DARK_GREEN
        self.width = 120
        self.height =16
        self.center_y = 250
        self.center_x = 750
        self.speed = 10
    def draw (self):
        arcade.draw_rectangle_filled(self.center_x,
        self.center_y,
        self.height,
        self.width,
        self.color)
class L_paddle:
    def __init__(self):
        super().__init__()
        self.color = arcade.color.DARK_GREEN
        self.width = 120
        self.height =16
        self.center_y = 250
        self.center_x = 50
        self.speed = 10
    def draw (self):
        arcade.draw_rectangle_filled(self.center_x,
        self.center_y,
        self.height,
        self.width,
        self.color)