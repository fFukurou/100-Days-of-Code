import random
from turtle import Turtle, Screen
from types import new_class
screen = Screen()


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.035
        self.bounce_randomizer = 0

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.bounce_randomizer = random.randint(-3, 3)
        self.y_move = self.y_move * -1 + self.bounce_randomizer
        self.x_move *= -1
        self.move_speed /= 1.3

    def reset_pos(self):
        self.bounce_randomizer = 0
        up_down = [-5, 5]
        self.goto(0, 0)
        self.move_speed = 0.035
        self.x_move *= -1
        self.y_move = random.choice(up_down)

    def reset_pos_l(self):
        self.reset_pos()

    def reset_pos_r(self):
        self.reset_pos()
