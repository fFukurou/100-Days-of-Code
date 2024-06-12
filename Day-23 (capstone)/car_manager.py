import random
from turtle import Turtle
from scoreboard import Scoreboard

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

cars = []

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        random_y = random.randint(-250, 250)
        self.penup()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.move_speed = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * Scoreboard.current_level)
        self.goto(300, random_y)
        cars.append(self)

    def move(self):
        self.goto(self.xcor() - self.move_speed, self.ycor())

    def increase_speed(self):   
        self.move_speed += MOVE_INCREMENT
