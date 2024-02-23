FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score_update(1)

    def score_update(self, s):
        self.goto(-250, 200)
        self.clear()
        self.write(arg=f"Level: {s}", align="left", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over.", align="center", font=("Courier", 30, "normal"))


