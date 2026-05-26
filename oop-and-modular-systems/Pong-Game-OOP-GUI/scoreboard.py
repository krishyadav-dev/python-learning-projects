from turtle import Turtle
FONT = ('Fixedsys', 20, 'normal')
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)




