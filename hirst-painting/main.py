import turtle as turtle_module
import random
# import colorgram
#
# colors = colorgram.extract('HirstD-PyroninY_700_480x480.jpg', 30)
# print(colors)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(226, 147, 97), (24, 104, 181), (154, 78, 45), (178, 16, 38), (160, 55, 94), (244, 226, 94), (226, 61, 98), (109, 174, 218), (233, 79, 48), (223, 126, 158), (9, 174, 209), (120, 184, 130), (13, 56, 150), (166, 152, 21), (81, 32, 19), (129, 35, 25), (38, 128, 78), (41, 190, 149), (242, 164, 151), (11, 34, 94), (235, 162, 182), (123, 237, 191), (86, 103, 199), (128, 215, 240), (79, 27, 46), (72, 80, 30)]

turtle = turtle_module.Turtle()
PACE = 50
turtle.speed('fastest')
turtle_module.colormode(255)

turtle.teleport(-250, -250)
turtle.setheading(0)
for row in range(10):
    turtle.teleport(-250, turtle.ycor()+PACE)
    for spot in range(10):
        color = random.choice(color_list)
        turtle.color(color)
        turtle.dot(20)
        turtle.up()
        turtle.forward(PACE)
        turtle.down()
turtle.hideturtle()

screen = turtle_module.Screen()
screen.exitonclick()