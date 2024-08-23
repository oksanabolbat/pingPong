from turtle import Turtle


class ScorePoints(Turtle):
    def __init__(self, player):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("#fff")
        if player == "l":
            self.goto(-100, 220)
        else:
            self.goto(100, 220)
        self.score_points = 0
        self.write(self.score_points, align="center", font=("Courier", 50, "normal"))

    def update_score(self):
        self.clear()
        self.write(self.score_points, align="center", font=("Courier", 50, "normal"))

    def add_point(self):
        self.score_points += 1
        self.update_score()
