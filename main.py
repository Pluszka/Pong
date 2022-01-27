from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=900, height=600)
screen.title('Pong')
screen.bgcolor('black')

right_paddle = Paddle()
screen.listen()
screen.onkey(fun=right_paddle.move_up, key='Up')
screen.onkey(fun=right_paddle.move_down, key='Down')

screen.exitonclick()