#Turtle Crossing Project

import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager, cars
from scoreboard import Scoreboard, FONT

ticks = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

score = Scoreboard()
player = Player()

screen.listen()
screen.onkeypress(player.move, 'w')



game_is_on = True
while game_is_on:
    if ticks % 6 == 0:
        car = CarManager()
    time.sleep(0.07)
    screen.update()
    for car in cars:
        car.move()

    if player.check_car_collision() == True:
        game_is_on = False

    if player.check_finish_line() == True:
        score.increase_level()
        for car in cars:
            car.increase_speed()
    
    ticks += 1

score.update_scoreboard()
score.goto(0, 0)
score.write(f"GAME OVER", align='center', font=FONT)

screen.exitonclick()

