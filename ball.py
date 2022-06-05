import random
import arcade
class Ball:
    def __init__(self):
        super().__init__()
        self.color = arcade.color.RED
        self.center_y = 250
        self.center_x = 400
        self.speed = 10
        self.radius = 10      
    def draw (self):
        arcade.draw_circle_filled(self.center_x,
        self.center_y,
        self.radius,
        self.color)