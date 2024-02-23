import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle


class CarManager(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)

        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.showturtle()

    def move(self, level):
        speed = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT*(level - 1))
        self.forward(speed)
