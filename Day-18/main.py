import random
import turtle
from turtle import Turtle, Screen
aamai = Turtle()
screen = Screen()
aamai.color('green')
turtle.colormode(255)

#square
# for i in range(4):
#     aamai.forward(100)
#     aamai.right(90)


#dotted lines
# for i in range(20):
#     for _ in range(2):
#         aamai.pensize(i)
#         aamai.forward(i)
#         if i % 2 == 0:
#             aamai.pendown()
#         else:
#             aamai.penup()


#3 to 10 shapes
# sides = 3
# colours = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red', 'pink']
# # angles = [120, 90, 108*2, 120, 128.57, 135, 140, 144]
#
# for color in range(8):
#     aamai.pencolor(colours[color])
#     for i in range(sides):
#         aamai.forward(60)
#         aamai.right(360/sides)
#     sides += 1


#random walk
# colours = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red', 'pink']
# while True:
#     aamai.pensize(10)
#     aamai.pencolor((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
#     aamai.speed('fastest')
#     choice_move = random.randint(1,2)
#     choice_angle = random.randint(1,2)
#     if choice_move == 1:
#         aamai.forward(20)
#     else:
#         aamai.back(20)
#
#     if choice_angle == 1:
#         aamai.right(90)
#     else:
#         aamai.left(90)


#drawing a spirograph
# aamai.speed('fastest')
# for i in range(int(360/5)):
#     aamai.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#     aamai.circle(100)
#     aamai.setheading(aamai.heading() + 5)
for i in range(10):
    for j in range(10):
        aamai.dot(20, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        if i % 2 == 0:
            aamai.forward(20)
        else:
            aamai.back(20)
    if i % 2 == 0:
        aamai.right(90)
        aamai.forward(20)
        aamai.right(90)
    else:
        aamai.left(90)
        aamai.forward(20)
        aamai.left(90)

screen.exitonclick()
