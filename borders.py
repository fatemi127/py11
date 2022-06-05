import random
import arcade
border_thickness = 6
class R_border:
    def __init__(self):
        super().__init__()
        self.color = arcade.color.RED
        self.width = border_thickness
        self.height =500
        self.center_y = 250
        self.center_x = 800
    def draw (self):
        arcade.draw_rectangle_filled(
        self.center_x,
        self.center_y,
        self.width,
        self.height,
        self.color)     
#buttom:
class B_border:
    def __init__(self):
        super().__init__()
        self.color = arcade.color.GREEN
        self.width = 800
        self.height =border_thickness
        self.center_y = 0
        self.center_x = 400
    def draw (self):
        arcade.draw_rectangle_filled(
        self.center_x,
        self.center_y,
        self.width,
        self.height,
        self.color) 
        #top:
class T_border:
    def __init__(self):
        super().__init__()
        self.color = arcade.color.GREEN
        self.width = 800
        self.height =border_thickness
        self.center_y = 500
        self.center_x = 400
    def draw (self):
        arcade.draw_rectangle_filled(
        self.center_x,
        self.center_y,
        self.width,
        self.height,
        self.color)     
class L_border:
    def __init__(self):
        super().__init__()
        self.color = arcade.color.BLUE
        self.width = border_thickness
        self.height =500
        self.center_y = 250
        self.center_x = 0
    def draw (self):
        arcade.draw_rectangle_filled(
        self.center_x,
        self.center_y,
        self.width,
        self.height,
        self.color)     
class Middle_line:
    def __init__(self):
        super().__init__()
        self.color = arcade.color.GREEN
        self.width = border_thickness
        self.height =500
        self.center_y = 250
        self.center_x = 400
    def draw (self):
        arcade.draw_rectangle_filled(
        self.center_x,
        self.center_y,
        self.width,
        self.height,
        self.color)     