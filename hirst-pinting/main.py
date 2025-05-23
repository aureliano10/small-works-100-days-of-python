import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
color_list = [(235, 226, 87), (210, 161, 109), (113, 177, 212), (201, 5, 68), (230, 52, 128), (196, 77, 19), (217, 133, 177), (193,
                                                                                                                 164,
                                                                                                                 15), (
    34, 106, 166), (11, 21, 62), (32, 189, 114), (232, 224, 4), (18, 28, 171), (122, 188, 161), (204, 32, 127), (233,
                                                                                                                 165,
                                                                                                                 197), (
    14, 183, 211), (10, 45, 24), (38, 132, 72), (45, 15, 10), (105, 92, 210), (139, 219, 203), (185, 13, 6), (135, 218,
                                                                                                              232), (
    229, 73, 45), (169, 180, 229)]

tom = Turtle()
tom.speed(10)
possiton_y = -250
for i in range(10):
    tom.penup()
    tom.goto(-250, possiton_y)
    for _ in range(10):
        tom.dot(20, random.choice(color_list))
        tom.fd(50)
    possiton_y += 50

screen = Screen()
screen.exitonclick()