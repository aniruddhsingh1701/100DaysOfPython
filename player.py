STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.start_level()

    def start_level(self):
        self.hideturtle()
        self.goto(0, -230)
        self.showturtle()

    def up(self):
        self.forward(10)