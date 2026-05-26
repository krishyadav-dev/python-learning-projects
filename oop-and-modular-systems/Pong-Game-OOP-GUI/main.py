import time
from turtle import Screen
from pong_ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

# ---Class Initialization---
screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
r_scoreboard = Scoreboard((170, 270))
l_scoreboard = Scoreboard((-170, 270))
ball = Ball()

# ---Screen Setup
screen.tracer(0)
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")

# ---Game Setup---
game_is_on = True
bounces = 0

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

def reset_positions():
    r_paddle.reset_position()
    l_paddle.reset_position()
    ball.reset_position()
    screen.update()

# ---Main Game Loop---

while game_is_on:
    ball.move_forward()
    screen.update()
    time.sleep(ball.move_speed)
    #Detect collision with vertical boundaries
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_rebound()

    #Detect collision with rpaddle
    if ball.distance(r_paddle) < 55 and 316 < ball.xcor() < 340 and (ball.heading() < 90 or ball.heading() > 270):
        ball.paddle_rebound()
        bounces += 1

    #Detect collision with lpaddle
    if ball.distance(l_paddle) < 55 and -340 < ball.xcor() < -316 and 90 < ball.heading() < 270:
        ball.paddle_rebound()
        print("Collision with left paddle!")
        bounces += 1

    #Detect a miss by R paddle
    if ball.xcor() > 380:
        l_scoreboard.increase_score()
        reset_positions()
        time.sleep(1.5)

    #Detect a miss by L paddle
    if ball.xcor() < -380:
        r_scoreboard.increase_score()
        reset_positions()
        time.sleep(1.5)

    if bounces % 2 == 0 and bounces != 0:
        bounces = 0
        ball.change_speed()
        print("speed is " + str(ball.move_speed))


screen.exitonclick()