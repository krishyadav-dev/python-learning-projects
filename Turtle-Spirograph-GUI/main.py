import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")

# Draw a Square
# for num in range(4):
#     tim.forward(100)
#     tim.left(90)

# Draw a dashed line
# for num in range(6):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()

# # Draw different Shapes:
# def draw_shape(num_sides):
#
#     for num in range(num_sides):
#         angle = 360/num_sides
#         tim.forward(100)
#         tim.right(angle)
#
# i=0
# for _ in range(3,11):
#     colors = ["black", "red", "blue", "green", "orange", "purple", "yellow", "deep pink", "purple", "dark orchid", "indigo", "medium slate blue"]
#     tim.color(colors[i])
#     i+=1
#     draw_shape(_)

# Random RGB Generator
def random_color():
    r = random.randint(0,255)
    g = 0#random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r,g,b)
    return r_color

# # Random Walk
turtle.colormode(255)
# direction = {
#     "north" : 0,
#     "south" : 180,
#     "east" : 90,
#     "west" : 270
# }
# tim.width(7)
# colors = ["black", "red", "blue", "green", "orange", "purple", "yellow", "deep pink", "purple", "dark orchid", "indigo", "medium slate blue"]
tim.speed("fastest")
#
# for num in range(1000):
#     random_dir = random.choice(list(direction.values()))
#     tim.color(random_color())
#     tim.seth(random_dir)
#     tim.forward(25)

tim.teleport(0, -60)
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(150)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(2)

screen = Screen()
screen.exitonclick()