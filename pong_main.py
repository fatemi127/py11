import random
import arcade
from ball import Ball
from paddles import R_paddle,L_paddle
from borders import R_border,L_border,T_border,B_border,Middle_line
spd = 25
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width= 800, height= 500, title = "Hossein's Pong Game!", resizable=True)
        self.background_color = arcade.color.SAFFRON
        # self.food = Apple()
        self.R_paddle = R_paddle()
        self.L_paddle = L_paddle()
        self.R_border = R_border()
        self.T_border = T_border()
        self.B_border = B_border()
        self.L_border = L_border()
        self.Middle_line = Middle_line()

        self.Ball = Ball()
        self.score = 0
    def hit (self):
        self.score += 1
        print (self.score)
    def on_draw(self):
        arcade.start_render()
        # self.food.draw()
        self.R_paddle.draw()
        self.L_paddle.draw()
        self.R_border.draw()
        self.T_border.draw()
        self.B_border.draw()
        self.L_border.draw()
        self.Middle_line.draw()
        self.Ball.draw()
        #buttons:
    def on_key_press(self,symbol:int, modifiers: int):
        if symbol == arcade.key.UP:
            self.R_paddle.center_y += spd
        elif symbol == arcade.key.W:
            self.L_paddle.center_y += spd
        elif symbol == arcade.key.DOWN:
            self.R_paddle.center_y -= spd
        elif symbol == arcade.key.S:
            self.L_paddle.center_y -= spd
    
    # def on_update(self,delta_time):
    #     if arcade.check_for_collision(self.Ball,self.L_border):
    #         self.Ball.hit()
            
g = Game()
arcade.run()