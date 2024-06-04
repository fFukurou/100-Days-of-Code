#Snake Game Project Part 2

import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

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

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score += 1
        score.refresh()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
