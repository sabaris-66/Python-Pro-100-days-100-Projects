from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')



aamai = Turtle()

screen.tracer(0)
python = Snake()
snack = Food()
actual_score = scoreboard()
snack.placement()
game_is_on = True
next_food = False

while game_is_on:
    screen.update()
    time.sleep(0.1)
    if next_food:
        snack.placement()
    screen.listen()
    screen.onkey(fun=python.turn_left, key='a')
    screen.onkey(fun=python.turn_right, key='d')
    screen.onkey(fun=python.turn_up, key='w')
    screen.onkey(fun=python.turn_down, key='s')
    python.move()
    if python.part[0].distance(snack.food) < 15:
        next_food = True
        actual_score.increase_score()
    else:
        next_food = False


screen.exitonclick()
