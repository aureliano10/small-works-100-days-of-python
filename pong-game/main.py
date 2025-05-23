from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

player_1 = Paddle((350, 0))
player_2 = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(player_1.up, "Up")
screen.onkey(player_1.down, "Down")
screen.onkey(player_2.up, "w")
screen.onkey(player_2.down, "s")

game_is_on = True
while game_is_on:

    screen.update()
    player_1.paddle_limit()
    player_2.paddle_limit()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detectart colision con jplayer 1
    if ball.distance(player_1) < 50 and ball.xcor() > 320 or ball.distance(player_2) < 50 and ball.xcor() < -320:
        ball.increase_speed()
        ball.bounce_x()

    #detectar punto
    if ball.xcor() > 370:
        score.player_2_score()
        ball.reset_position()
    elif ball.xcor() < -370:
        score.player_1_score()
        ball.reset_position()


    ball.move()
    time.sleep(ball.speed_ball)












screen.exitonclick()