from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=900, height=600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(0)

right_paddle = Paddle(375)
left_paddle = Paddle(-375)

screen.listen()
screen.onkey(fun=right_paddle.move_up, key='Up')
screen.onkey(fun=right_paddle.move_down, key='Down')
screen.onkey(fun=left_paddle.move_up, key='w')
screen.onkey(fun=left_paddle.move_down, key='s')

game_on = True

while game_on:
    screen.update()
screen.exitonclick()