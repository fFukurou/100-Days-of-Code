#Pong Project

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.title('Pong')
screen.bgcolor('black')
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #Detect collision with wall
    if (ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce_wall()


    #Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()


    #Detect if R paddle misses
    if ball.xcor() > 400:
        ball.reset_pos_l()
        scoreboard.l_point()


    #Detect if L paddle misses
    if ball.xcor() < -400:
        ball.reset_pos_r()
        scoreboard.r_point()

screen.exitonclick()