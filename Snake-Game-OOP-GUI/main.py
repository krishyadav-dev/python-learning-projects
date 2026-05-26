from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

# --- Screen Setup ---
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# --- Class Initialization ---
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# --- Main Game Loop ---
game_is_on = True

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


while game_is_on:
    snake.move_snake()
    screen.update()
    time.sleep(0.08)

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

        #Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()






screen.exitonclick()