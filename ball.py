from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#fff")
        self.penup()
        # time.sleep(0.3)
        self.step_x = 10
        self.step_y = 10
        self.move_speed = 0.1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.step_y *= -1


    def move(self):
        self.goto(self.xcor() + self.step_x, self.ycor() + self.step_y)

    def bounce_y(self):
        self.step_y *= -1
        self.move_speed *= 0.9
    def bounce_x(self):
        self.step_x *= -1
        self.move_speed *= 0.9


