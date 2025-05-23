import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
tom = Turtle()
tom.shape("turtle")
tom.speed(10)

tom.pensize(2)

movements = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_the_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tom.pencolor(random_color())
        current_heading = tom.heading()
        tom.setheading(current_heading + size_of_gap)
        tom.circle(100, 360)

draw_the_spirograph(30)




screen = Screen()
screen.exitonclick()