from turtle import Turtle


class Snake:

    def __init__(self):
        self.part = None
        self.x = 0
        self.position()

    def position(self):
        self.part = []
        for _ in range(3):
            new_segment = Turtle("square")
            new_segment.color('white')
            new_segment.pencolor('orange')
            new_segment.penup()
            new_segment.goto(x=self.x, y=0)
            self.part.append(new_segment)
            self.x -= 20

    def turn_up(self):
        if self.part[0].heading() != 270:
            self.part[0].setheading(90)

    def turn_left(self):
        if self.part[0].heading() != 0:
            self.part[0].setheading(180)

    def turn_down(self):
        if self.part[0].heading() != 90:
            self.part[0].setheading(270)

    def turn_right(self):
        if self.part[0].heading() != 180:
            self.part[0].setheading(0)

    def move(self):
        for segment in range(len(self.part) - 1, 0, -1):
            x_cor = self.part[segment - 1].xcor()
            y_cor = self.part[segment - 1].ycor()
            self.part[segment].goto(x_cor, y_cor)
        self.part[0].forward(20)
