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
        self.score_text()

    def score_text(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT , font=FONT )

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_text()