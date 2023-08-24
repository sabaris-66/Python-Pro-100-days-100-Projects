import colorgram
import turtle as t
import random
t.colormode(255)
aamai = t.Turtle()
screen = t.Screen()

#colorgram work
colors = colorgram.extract('dotttttt.jpg', 20)
color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r, g, b))
color_list = color_list[3:]

#turtle work
def home_position():
    aamai.penup()
    aamai.back(50 * 10)
    aamai.right(90)
    aamai.forward(50)
    aamai.left(90)
    aamai.pendown()
def start_position():
    aamai.penup()
    aamai.back(50*7)
    aamai.left(90)
    aamai.forward(50*5)
    aamai.right(90)
    aamai.pendown()


def main():
    aamai.speed('fastest')
    start_position()
    for i in range(10):
        for j in range(10):
            aamai.dot(20, random.choice(color_list))
            aamai.penup()
            aamai.forward(50)
        home_position()
    aamai.hideturtle()

main()

screen.exitonclick()