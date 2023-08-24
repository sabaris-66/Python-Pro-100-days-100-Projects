from turtle import Turtle
import random
from snake import Snake

class Food:
    def __init__(self):
        self.food = None
        self.preparation()
    def preparation(self):
        self.food = Turtle('circle')
        self.food.color('blue')
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food.penup()
        # self.food.hideturtle()

    def placement(self):
        self.food.goto(random.randint(-300, 300), random.randint(-300, 300))
        # self.food.showturtle()

    # def hide(self):
    #     self.food.hideturtle()
