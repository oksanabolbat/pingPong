from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, paddle_cors):
        super().__init__()
        self.penup()
        self.color("#fff")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(paddle_cors)

    def move_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 20)
        # print(f"{self.paddle_type} up")

    def move_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)
