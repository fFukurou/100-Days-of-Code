from turtle import Turtle
from typing import Self
from car_manager import cars


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('blue')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def check_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True

    def check_car_collision(self):
        for car in cars:
            if car.distance(self) < 25:
                return True