from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet: ", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange","yellow","green", "blue","purple"]
START_LOC = -100
all_turtles = []
is_race_on = False

for turtle_index in range (6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.up()
    new_turtle.goto(x=-230, y=START_LOC)
    START_LOC += 33
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color  == user_bet:
                    print(f"You've Won! The {winning_color} turtle is the winner.")
                else:
                    print(f"You've Lost! The {winning_color} turtle is the winner.")
            rand_distance = random.randint(2,10)
            turtle.forward(rand_distance)


screen.exitonclick()