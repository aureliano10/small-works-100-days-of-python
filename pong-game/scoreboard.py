from turtle import Turtle

FONT = ("Courier", 20, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 230)
        self.pencolor("white")
        self.score1 = 0
        self.score2 = 0
        self.write_score()

    def write_score(self):
        self.write(f"SCORE\n{self.score2} | {self.score1}", align="center", font=FONT)

    def player_2_score(self):
        self.score2 += 1
        self.clear()
        self.write_score()

    def player_1_score(self):
        self.score1 += 1
        self.clear()
        self.write_score()