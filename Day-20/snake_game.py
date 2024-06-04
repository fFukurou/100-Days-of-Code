import time
from tracemalloc import Snapshot
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.left, 'a')
screen.onkey(snake.down, 's')
screen.onkey(snake.right, 'd')


screen.update()

game_is_on= True

while game_is_on:
    screen.update()
    time.sleep(0.075)

    snake.move()

screen.exitonclick()