from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

r_col = '#EB5E28'
l_col = "#CCC5B9"

screen = Screen()
screen.setup(width=900, height=600)
screen.title('Pong')
screen.bgcolor('#252422')
screen.tracer(0)

right_paddle = Paddle(375, r_col)
left_paddle = Paddle(-375, l_col)
ball = Ball()
r_score = Score(30, r_col)
l_score = Score(-30, l_col)

screen.listen()
screen.onkey(fun=right_paddle.move_up, key='Up')
screen.onkey(fun=right_paddle.move_down, key='Down')
screen.onkey(fun=left_paddle.move_up, key='w')
screen.onkey(fun=left_paddle.move_down, key='s')

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(right_paddle) < 60 and ball.xcor() > 360:
        ball.bounce_x()

    elif ball.distance(left_paddle) < 60 and ball.xcor() < -360:
        ball.bounce_x()
    else:
        if ball.xcor() < -450:
            ball = Ball()
            r_score.updateScore()
        elif ball.xcor() > 450:
            ball = Ball()
            ball.bounce_x()
            l_score.updateScore()
screen.exitonclick()
