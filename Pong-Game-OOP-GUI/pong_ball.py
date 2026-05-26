from turtle import Turtle
from random import randint, choice
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        launch_angle = [randint(20, 60), randint(300, 340), randint(120, 160), randint(200, 240)]
        self.angle =  choice(launch_angle)
        self.move_speed = 0.05

    def move_forward(self):
        self.setheading(self.angle)
        self.forward(10)

    def wall_rebound(self):
        self.angle = 0
        self.angle += -(self.heading())

    def paddle_rebound(self):
        self.angle = 180 - self.heading()

    def reset_position(self):
        self.goto(0,0)

    def change_speed(self):
        if self.move_speed > 0.03:
            self.move_speed -= 0.005
