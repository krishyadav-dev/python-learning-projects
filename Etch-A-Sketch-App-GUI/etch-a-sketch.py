from turtle import  Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_counterclockwise():
    tim.left(5)
def turn_clockwise():
    tim.right(5)
def clearscreen():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_clockwise,key="d")
screen.onkey(fun=turn_counterclockwise,key="a")
screen.onkey(fun=clearscreen, key="c")

screen.exitonclick()