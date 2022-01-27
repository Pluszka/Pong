from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


screen = Screen()
screen.setup(width=900, height=600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(0)

right_paddle = Paddle(375)
left_paddle = Paddle(-375)
ball = Ball()
r_score = Score(30)
l_score = Score(-30)

screen.listen()
screen.onkey(fun=right_paddle.move_up, key='Up')
screen.onkey(fun=right_paddle.move_down, key='Down')
screen.onkey(fun=left_paddle.move_up, key='w')
screen.onkey(fun=left_paddle.move_down, key='s')

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()



    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(right_paddle) < 60 and ball.xcor() > 360:
        ball.bounce_x()

    if ball.distance(left_paddle) < 60 and ball.xcor() < -360:
        ball.bounce_x()

    if ball.xcor() < -450:
        ball = Ball()
    elif ball.xcor() > 450:
        ball = Ball()

screen.exitonclick()