# from turtle import Turtle, Screen
#
# nandha = Turtle()
# nandha.color('blue')
# nandha.shape('turtle')
# nandha.shapesize(5)
# print(nandha)
# my_screen = Screen()
# print(my_screen.canvheight)
# for i in ['red', 'blue', 'green']:
#     nandha.color(i)
#     nandha.forward(100)
#     nandha.left(120)
#     nandha.forward(100)
#
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("pokemon", ['pikachu', 'charizad','squirtle', 'bulbasar'])
table.add_column("type", ['electric', 'fire', 'water', 'grass'])
table.align = 'c'
print(table)
