from turtle import Turtle, Screen
aamai = Turtle()
screen = Screen()


def move_for():
    aamai.forward(20)
def move_back():
    aamai.back(20)
def anti_clock():
    aamai.left(20)
def clock():
    aamai.right(20)
def clear():
    aamai.home()
    aamai.clear()


screen.listen()
screen.onkey(key='w', fun=move_for)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='a', fun=anti_clock)
screen.onkey(key='d', fun=clock)
screen.onkey(key='c', fun=clear)
screen.exitonclick()