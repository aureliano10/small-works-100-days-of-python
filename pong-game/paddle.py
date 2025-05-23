from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.create_paddle(pos)
        self.paddle_limit()

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.turtlesize(stretch_len=5.0)

    def paddle_limit(self):
        if self.ycor() >= 250:
            self.sety(249)

        elif  self.ycor() <= -250:
            self.sety(-249)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)