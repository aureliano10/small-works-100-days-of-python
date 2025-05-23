import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, key="Up")

carmanager = CarManager()

game_is_on = True
while game_is_on:
    carmanager.create_car()
    carmanager.move_cars()

    for car in carmanager.cars:
        if car.distance(player) <= 20:
            scoreboard.game_over()
            game_is_on = False

    #detectar punto
    if player.ycor() >= 280:
        player.point()
        scoreboard.increase_score()
        carmanager.restart()
        carmanager.level_up()

    time.sleep(0.1)
    screen.update()






screen.exitonclick()