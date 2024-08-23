from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorePoints import ScorePoints
import time

screen = Screen()
screen.setup(800,600)
screen.title("Pong")
screen.bgcolor("#000")
screen.tracer(0)

left_paddle = Paddle((-380,0))
right_paddle = Paddle((370, 0))
# screen.update()
screen.listen()
# screen.tracer(1)

screen.onkey(left_paddle.move_down, "space")
screen.onkey(left_paddle.move_up, "c")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

ball = Ball()
game_is_on = True

score_l = ScorePoints("l")
score_r = ScorePoints("r")

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()
    if ball.xcor() > 340 and ball.distance(right_paddle) < 50 or ball.xcor() < -350 and ball.distance(left_paddle) < 50:
        ball.bounce_x()
    if ball.xcor() > 400:
        ball.reset_position()
        ball.bounce_x()
        score_l.add_point()
    if ball.xcor() < -400:
        ball.reset_position()
        ball.bounce_x()
        score_r.add_point()
    screen.update()

screen.exitonclick()