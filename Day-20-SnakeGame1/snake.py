import time
from turtle import Screen, Turtle
MOVES_SPEED = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0



class Snake:
    def __init__(self) -> None:
        self.initial_x_position = 0
        self.segments = []
        

        for x in range(0, 3):
            self.square = Turtle('square')
            self.square.penup()
            self.square.color('white')
            self.square.goto(self.initial_x_position, 0)
            self.initial_x_position -= 20
            self.segments.append(self.square)

        self.head = self.segments[0]


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