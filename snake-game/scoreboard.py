import turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.pencolor("white")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score_text()


    def score_text(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT , font=FONT )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.score_text()

    def increase_score(self):
        self.score += 1
        self.score_text()