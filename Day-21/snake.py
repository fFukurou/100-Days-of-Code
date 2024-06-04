import time
from turtle import Screen, Turtle
MOVES_SPEED = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
STARING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]



class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
            self.square = Turtle('square')
            self.square.penup()
            self.square.color('white')
            self.square.goto(position)
            self.segments.append(self.square)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVES_SPEED) 

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)