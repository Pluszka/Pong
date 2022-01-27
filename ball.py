from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball = self.create()
        self.x_move = 10
        self.y_move = 10


    def create(self):
        new = Turtle()
        new.shape('square')
        new.penup()
        new.color('white')
        new.shapesize(stretch_wid=0.5, stretch_len=0.5)
        return new


    def move(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1