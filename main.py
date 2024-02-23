import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=500)
screen.tracer(0)
screen.listen()
level = 1
score_board = Scoreboard()

gamer = Player()
screen.onkey(gamer.up, "Up")
game_is_on = True
obstacles = []
create_obstacles = 0
while game_is_on:
    create_obstacles += 1
    time.sleep(0.1)
    score_board.score_update(level)
    if create_obstacles % (20/level) < 1:
        for _ in range(random.randint(2, 5)):
            x = 330
            y = random.randrange(-180, 180, 20)
            obstacle = CarManager(x, y)
            obstacles.append(obstacle)
    for obstacle in obstacles:
        if obstacle.distance(gamer) < 20:
            score_board.game_over()
            print("over")
            game_is_on = False

        else:
            obstacle.move(level)


    if gamer.ycor() > 240:
        gamer.start_level()
        level += 1
    screen.update()
screen.exitonclick()